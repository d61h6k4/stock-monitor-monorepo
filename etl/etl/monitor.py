from datetime import datetime, timedelta
import json
import os
import time

from requests import HTTPError
import psycopg
from typing import Any, Iterable, Mapping, Sequence, Set, Tuple

from bytewax.connectors.kafka import KafkaInput
from bytewax.dataflow import Dataflow
from bytewax.outputs import DynamicOutput, StatelessSink
from etl.notifyer import NotificationCenter
from etl.telegram.client import TelegramClient
from etl.rules import (
    Action,
    Decision,
    adx_rule,
    macd_rule,
    rsi_rule,
    mfi_rule,
    swing_low_rule,
    coppock_curve_rule,
)


class NotifierSink(StatelessSink):
    def __init__(self, telegram_bot_token: str):
        super().__init__()

        self.telegram_client = TelegramClient(token=telegram_bot_token)
        self.notify = NotificationCenter()
        self.notify.add_telegram(self.telegram_client)

    def close(self):
        self.notify.persist()

    def write_batch(self, items: Iterable[Tuple[str, Decision]]):
        for key__payload in items:
            _, decision = key__payload
            try:
                self.notify.send_unique_decision("dbihbka", decision)
            except HTTPError:
                time.sleep(2)


class NotifierOutput(DynamicOutput):
    def __init__(self, telegram_bot_token: str) -> None:
        super().__init__()
        self.telegram_bot_token = telegram_bot_token

    def build(self, worker_index: int, worker_count: int) -> NotifierSink:
        return NotifierSink(self.telegram_bot_token)


def notify():
    DB_HOST = os.getenv("POSTGRES_HOST")
    DB_USER = os.getenv("POSTGRES_USER")
    DB_NAME = os.getenv("POSTGRES_DB")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")

    BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "localhost:19092").split(",")
    KAFKA_INPUT_TOPICS = os.getenv("KAFKA_INPUT_TOPICS", "features").split(",")

    telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    assert telegram_bot_token, "Missing TELEGRAM_BOT_TOKEN"

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

    def apply_rules(
        key__payload: Tuple[str, Mapping[str, Any]]
    ) -> Sequence[Tuple[str, Decision]]:
        key, payload = key__payload
        return [
            (key, decision)
            for decision in [
                macd_rule(
                    payload["symbol"],
                    payload["close"],
                    payload["macd"],
                    payload["macd_signal"],
                ),
                adx_rule(
                    payload["symbol"],
                    payload["close"],
                    payload["pdi"],
                    payload["ndi"],
                    payload["adx"],
                ),
                rsi_rule(payload["symbol"], payload["close"], payload["rsi"]),
                mfi_rule(
                    payload["symbol"],
                    current_price=payload["close"],
                    pct_change=payload["pct_change"],
                    mfi_value=payload["money_flow_index"],
                    mfi_delta=payload["mfi_delta"],
                ),
                swing_low_rule(
                    payload["symbol"],
                    current_price=payload["close"],
                    swing_low=payload["swing_low"],
                ),
                coppock_curve_rule(
                    payload["symbol"],
                    current_price=payload["close"],
                    coppock_curve=payload["coppock_curve"],
                ),
            ]
        ]

    flow.flat_map(apply_rules)

    class FilterWithPortfolioInfo:
        def __init__(self, db_host: str, db_user: str, db_name: str, db_password: str):
            conn_info = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"
            self.connection = psycopg.connect(conn_info)

            self.last_update_time = datetime.now()
            self._portfolio = None

        @property
        def portfolio(self) -> Set[str]:
            if (
                self._portfolio is None
                or datetime.now() - self.last_update_time > timedelta(days=1)
            ):
                with self.connection.cursor() as cur:
                    cur.execute("SELECT symbol FROM tickers WHERE in_portfolio")
                    self._portfolio = set([x[0] for x in cur.fetchall()])

                self.last_update_time = datetime.now()
            return self._portfolio

        def __call__(self, key__payload: Tuple[str, Decision]) -> bool:
            symbol, decision = key__payload
            if symbol in self.portfolio and decision.action == Action.SELL:
                return True
            elif symbol not in self.portfolio and decision.action == Action.BUY:
                return True
            else:
                return False

    flow.filter(FilterWithPortfolioInfo(DB_HOST, DB_USER, DB_NAME, DB_PASSWORD))

    flow.output("notify", NotifierOutput(telegram_bot_token))

    return flow
