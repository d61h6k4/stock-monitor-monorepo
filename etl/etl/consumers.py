import json
import os
import psycopg

from typing import Any, Iterable, Mapping, Tuple

from bytewax.connectors.kafka import KafkaInput
from bytewax.dataflow import Dataflow
from bytewax.outputs import DynamicOutput, StatelessSink


class SQLSink(StatelessSink):
    def __init__(self, conn_info: str):
        super().__init__()

        self.connection = psycopg.connect(conn_info)

        self.prepare_tables()

    def prepare_tables(self):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS history (
                    record_id SERIAL PRIMARY KEY,
                    symbol VARCHAR(12) NOT NULL,
                    date DATE,
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
                    rsi REAL,
                    dividends REAL)
                """
            )
            self.connection.commit()
        print("Table history is created.")

    def close(self):
        self.cursor.close()
        self.connection.close()

    def write_batch(self, items: Iterable[Tuple[str, Mapping[str, Any]]]):
        records = []
        for key__payload in items:
            _, item = key__payload
            records.append(item)

        with self.connection.cursor() as cursor:
            cursor.executemany(
                """INSERT INTO 
                    history 
                    (
                        symbol, 
                        date, 
                        open, 
                        high, 
                        low, 
                        close, 
                        volume,
                        pdi, 
                        ndi, 
                        adx,
                        macd,
                        macd_signal,
                        rsi,
                        dividends
                    )
                   VALUES (
                        %(symbol)s, 
                        %(date)s, 
                        %(open)s, 
                        %(high)s, 
                        %(low)s, 
                        %(close)s, 
                        %(volume)s,
                        %(pdi)s, 
                        %(ndi)s, 
                        %(adx)s,
                        %(macd)s,
                        %(macd_signal)s,
                        %(rsi)s,
                        %(dividends)s
                    )
                """,
                records,
            )
            self.connection.commit()


class SQLOutput(DynamicOutput):
    def __init__(
        self, db_host: str, db_user: str, db_name: str, db_password: str
    ) -> None:
        super().__init__()
        self.conn_info = (
            f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"
        )

    def build(self, worker_index: int, worker_count: int) -> SQLSink:
        return SQLSink(self.conn_info)


def sink_to_db():
    DB_HOST = os.getenv("POSTGRES_HOST")
    DB_USER = os.getenv("POSTGRES_USER")
    DB_NAME = os.getenv("POSTGRES_DB")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "localhost:19092").split(",")
    KAFKA_INPUT_TOPICS = os.getenv("KAFKA_INPUT_TOPICS", "features").split(",")

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

    flow.output("sink_to_db", SQLOutput(DB_HOST, DB_USER, DB_NAME, DB_PASSWORD))

    return flow
