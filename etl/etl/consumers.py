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

        self.features = [
            "open",
            "high",
            "low",
            "close",
            "volume",
            "pdi",
            "ndi",
            "adx",
            "macd",
            "macd_signal",
            "rsi",
            "dividends",
            "moving_average_50",
            "moving_average_200",
            "money_flow_index",
            "swing_low",
            "coppock_curve",
        ]

        self.prepare_tables()

    def prepare_tables(self):
        features_schema = ",".join([f"{f} REAL" for f in self.features])
        with self.connection.cursor() as cursor:
            cursor.execute(
                f"""CREATE TABLE IF NOT EXISTS history (
                    record_id SERIAL PRIMARY KEY,
                    symbol VARCHAR(12) NOT NULL,
                    date DATE,
                    {features_schema})
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

        names = ",".join(self.features)
        values = ",".join([f"%({f})s" for f in self.features])
        with self.connection.cursor() as cursor:
            cursor.executemany(
                f"""INSERT INTO 
                    history 
                    (
                        symbol, 
                        date, 
                        {names}
                    )
                   VALUES (
                        %(symbol)s, 
                        %(date)s, 
                        {values}
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
