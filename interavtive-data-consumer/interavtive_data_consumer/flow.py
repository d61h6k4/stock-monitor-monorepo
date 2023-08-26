import json
import os
from sqlite3 import Connection
from typing import Any, Mapping, Tuple

from bytewax.connectors.kafka import KafkaInput
from bytewax.dataflow import Dataflow
from bytewax.outputs import DynamicOutput, StatelessSink

DB_URI = os.getenv("DB_URI", ":memory:")
BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "localhost:19092").split(",")
KAFKA_INPUT_TOPICS = os.getenv("KAFKA_INPUT_TOPICS", "features").split(",")


class SQLiteSink(StatelessSink):
    def __init__(self, db_uri: str):
        super().__init__()

        self.connection = Connection(db_uri)
        self.cursor = self.connection.cursor()

        self.prepare_tables()

    def prepare_tables(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS history (
                            symbol VARCHAR(10),
                            date TEXT,
                            open REAL,
                            high REAL,
                            low REAL,
                            close REAL,
                            volume REAL,
                            pdi REAL,
                            ndi REAL,
                            adx REAL,
                            macd REAL,
                            macd_signal REAL,
                            rsi REAL)
            """
        )

    def close(self):
        self.cursor.close()
        self.connection.close()

    def write(self, key__payload: Tuple[str, Mapping[str, Any]]):
        _, item = key__payload
        self.cursor.execute(
            """INSERT INTO 
                 history 
               VALUES (
                :symbol, 
                :date, 
                :open, 
                :high, 
                :low, 
                :close, 
                :volume,
                :pdi, 
                :ndi, 
                :adx,
                :macd,
                :macd_signal,
                :rsi
              )
            """,
            item,
        )
        self.connection.commit()


class SQLiteOutput(DynamicOutput):
    def __init__(self) -> None:
        super().__init__()

    def build(self, worker_index: int, worker_count: int) -> SQLiteSink:
        return SQLiteSink(DB_URI)


def sink_to_db():
    flow = Dataflow()
    flow.input(
        "events",
        KafkaInput(
            brokers=BOOTSTRAP_SERVERS,
            topics=KAFKA_INPUT_TOPICS,
        ),
    )

    def deserialize(raw_item_kv):
        item_v = json.loads(raw_item_kv[1])
        return item_v["symbol"], item_v

    flow.map(deserialize)

    flow.output("sink_to_db", SQLiteOutput())

    return flow
