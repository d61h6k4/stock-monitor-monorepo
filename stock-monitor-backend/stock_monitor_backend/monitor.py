from sched import scheduler

from stock_monitor_data import (
    crypto,
    etfs,
    ideas,
    oil_and_gas_stocks,
    portfolio,
)
from structlog import get_logger
from tqdm import tqdm

from stock_monitor_backend.notifyer import NotificationCenter
from stock_monitor_backend.rules import (
    Action,
    adx_rule,
    asr_rule,
    macd_rule,
    mad_rule,
    rsi_rule,
)
from stock_monitor_backend.telegram.client import TelegramClient

logger = get_logger(__name__)


class Monitor:
    def __init__(self, notifier, monitor_timedelta=3600, watch_timedelta=21600):
        self.monitor_timedelta = monitor_timedelta
        self.watch_timedelta = watch_timedelta

        self.notifier = notifier
        self.s = scheduler()

        self.s.enter(10, 1, self.start)
        self.s.run(blocking=True)

    def start(self):
        logger.info("Start monitoring ...")
        for idea in tqdm(
            ideas(period="3mo", interval="1d"), desc="Processing ideas..."
        ):
            self.watch(idea)
        for stock in tqdm(
            portfolio(period="3mo", interval="1d"), desc="Processing portfolio..."
        ):
            self.monitor(stock)
        for stock in tqdm(
            oil_and_gas_stocks(period="3mo", interval="1d"),
            desc="Processing Oil&Gas...",
        ):
            self.watch(stock)
        for stock in tqdm(
            crypto(period="3mo", interval="1d"), desc="Processing Crypto..."
        ):
            self.watch(stock)
        for stock in tqdm(etfs(period="3mo", interval="1d"), desc="Processing ETF..."):
            self.watch(stock)

    def notify(self, stock, actions):
        for rule in [
            asr_rule(stock.ticker_name),
            macd_rule(stock.ticker_name),
            rsi_rule(stock.ticker_name),
            adx_rule(stock.ticker_name),
            mad_rule(stock.ticker_name),
        ]:
            if rule.action in actions:
                self.notifier.send_unique_decision("dbihbka", rule)

    def watch(self, stock):
        logger.info(f"Watching {stock.ticker_name}...")
        self.s.enter(self.watch_timedelta, 1, self.notify, (stock, {Action.BUY}))
        self.s.enter(self.watch_timedelta, 2, self.watch, (stock,))

    def monitor(self, stock):
        logger.info(f"Monitoring {stock.ticker_name}...")
        self.s.enter(self.monitor_timedelta, 1, self.notify, (stock, {Action.SELL}))
        self.s.enter(self.monitor_timedelta, 2, self.monitor, (stock,))


def main():
    import os
    import signal

    telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    assert telegram_bot_token, "Missing TELEGRAM_BOT_TOKEN"
    telegram_client = TelegramClient(token=telegram_bot_token)
    notify = NotificationCenter()
    notify.add_telegram(telegram_client)
    signal.signal(signal.SIGTERM, lambda sig, frame: notify.persist())

    try:
        Monitor(notifier=notify)
    except BaseException as e:
        notify.persist()
        logger.error(repr(e))
