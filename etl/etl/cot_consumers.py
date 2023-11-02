from datetime import timedelta
import json
import logging
import os
import psycopg

from typing import Any, Iterable, Mapping, Tuple

from bytewax.connectors.kafka import KafkaInput
from bytewax.dataflow import Dataflow
from bytewax.outputs import DynamicOutput, StatelessSink


class SQLSink(StatelessSink):
    def __init__(self, conn_info: str, worker_index: int):
        super().__init__()

        self.logger = logging.getLogger(f"etl.cot_consumers.{worker_index}")
        self.connection = psycopg.connect(conn_info)

        self.features = [
            "open_interest_all",
            "prod_merc_positions_long_all",
            "prod_merc_positions_short_all",
            "swap_positions_long_all",
            "swap_positions_short_all",
            "m_money_positions_long_all",
            "m_money_positions_short_all",
            "other_rept_positions_long_all",
            "other_rept_positions_short_all",
            "nonrept_positions_long_all",
            "nonrept_positions_short_all",
        ]

        self.prepare_tables()

    def prepare_tables(self):
        features_schema = ",".join([f"{f} REAL" for f in self.features])
        with self.connection.cursor() as cursor:
            cursor.execute(
                f"""CREATE TABLE IF NOT EXISTS cot_history (
                    record_id SERIAL PRIMARY KEY,
                    market_and_exchange_names TEXT NOT NULL,
                    cftc_commodity_code INTEGER,
                    report_date DATE,
                    {features_schema})
                """
            )
            self.connection.commit()
        self.logger.info("Table cot_history is created.")

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
            try:
                cursor.executemany(
                    f"""INSERT INTO 
                    cot_history 
                    (
                        market_and_exchange_names,
                        cftc_commodity_code,
                        report_date,
                        {names}
                    )
                   VALUES (
                        %(market_and_exchange_names)s, 
                        %(cftc_commodity_code)s, 
                        %(report_date)s, 
                        {values}
                    )
                """,
                    records,
                )
            except Exception as e:
                self.logger.exception("Failed to insert %s", records)

                raise e from None

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
        return SQLSink(self.conn_info, worker_index)


def sink_to_db():
    DB_HOST = os.getenv("POSTGRES_HOST")
    DB_USER = os.getenv("POSTGRES_USER")
    DB_NAME = os.getenv("POSTGRES_DB")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "localhost:19092").split(",")
    KAFKA_INPUT_TOPICS = os.getenv("KAFKA_INPUT_TOPICS", "events").split(",")

    flow = Dataflow()
    flow.input(
        "events",
        KafkaInput(
            brokers=BOOTSTRAP_SERVERS,
            topics=KAFKA_INPUT_TOPICS,
        ),
    )

    def deserialize(key__payload):
        key, payload = key__payload
        return key, json.loads(payload)

    flow.map(deserialize)

    def is_cot_data(key__payload):
        _, payload = key__payload
        return "COMMITMENT_OF_TRADERS" == payload["kind"]

    flow.filter(is_cot_data)

    flow.batch("prebatch", 1000, timedelta(seconds=60))
    flow.output("sink_to_db", SQLOutput(DB_HOST, DB_USER, DB_NAME, DB_PASSWORD))

    return flow
