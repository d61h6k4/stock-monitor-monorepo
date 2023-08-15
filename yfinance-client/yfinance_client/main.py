import json
import logging
from argparse import ArgumentParser
from datetime import datetime
from itertools import chain
from pathlib import Path

from kafka import KafkaProducer
from rich.logging import RichHandler
from rich import progress

from yfinance_client.downloader import get_ticker_events, get_ticker_history_events


def stocks():
    from stock_monitor_data.cryptos import crypto
    from stock_monitor_data.etfs import etfs
    from stock_monitor_data.ideas import ideas
    from stock_monitor_data.oil_and_gas import oil_and_gas_stocks
    from stock_monitor_data.portfolio import portfolio

    yield from portfolio("1d", "1d")
    yield from oil_and_gas_stocks("1d", "1d")
    yield from etfs("1d", "1d")
    yield from crypto("1d", "1d")
    yield from ideas("1d", "1d")


def parse_args():
    parser = ArgumentParser()

    parser.add_argument(
        "--storage",
        type=Path,
        help="Specify path to the file to store the intermidiate data.",
        default=".storage.json",
    )
    parser.add_argument(
        "--kafka_bootstrap_servers",
        type=str,
        help="Specify kafka's bootstrap servers",
        default="localhost:19092",
    )
    parser.add_argument(
        "--kafka_topic",
        type=str,
        help="Specify the kafka topic stream to.",
        default="events",
    )

    return parser.parse_args()


def main():
    logging.basicConfig(handlers=[RichHandler()])
    logger = logging.getLogger("yfinance-client-cli")

    args = parse_args()

    if args.storage.exists():
        db = json.loads(args.storage.read_text())
    else:
        db = {}

    producer = KafkaProducer(
        bootstrap_servers=args.kafka_bootstrap_servers,
        value_serializer=lambda m: json.dumps(m).encode("utf8"),
    )

    def on_success(metadata):
        logger.info(
            f"Message produced to topic '{metadata.topic}'  at offset {metadata.offset}"
        )

    def on_error(e):
        logger.error(f"Error sending message: {e}")

    def send_event(event):
        future = producer.send(args.kafka_topic, value=event._asdict())
        future.add_callback(on_success)
        future.add_errback(on_error)

    with progress.Progress(
        "[progress.description]{task.description}",
        progress.BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        progress.TimeRemainingColumn(),
        progress.TimeElapsedColumn(),
        refresh_per_second=1,  # bit slower updates
    ) as pgs:
        process_stocks_task = pgs.add_task("[green]Processing stocks:", total=None)
        for stock in stocks():
            events = [get_ticker_events(symbol=stock.ticker_name)]
            if stock.ticker_name not in db:
                events.append(
                    get_ticker_history_events(symbol=stock.ticker_name)
                )

            process_events_task = pgs.add_task(
                f"Processing {stock.ticker_name}", total=None
            )
            for event in chain.from_iterable(reversed(events)):
                send_event(event)
                pgs.update(process_events_task)
            pgs.update(process_events_task, visible=False)

            db[stock.ticker_name] = {"last_update": datetime.today().isoformat()}
            pgs.update(process_stocks_task)

    args.storage.write_text(json.dumps(db))


if __name__ == "__main__":
    main()
