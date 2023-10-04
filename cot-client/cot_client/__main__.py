import json
import logging
from argparse import ArgumentParser
from os import getenv

from rich import progress
from rich.logging import RichHandler

from cot_client.downloader import historical_cot_report, latest_cot_report


def parse_args():
    parser = ArgumentParser()

    parser.add_argument(
        "--historical",
        action="store_true",
        help="Specify wether to load historical data or new one.",
    )
    parser.add_argument(
        "--kafka_bootstrap_servers",
        type=str,
        help="Specify kafka's bootstrap servers",
        default=getenv("BOOTSTRAP_SERVERS"),
    )
    parser.add_argument(
        "--kafka_topic",
        type=str,
        help="Specify the kafka topic stream to.",
        default="events",
    )

    return parser.parse_args()


def main():
    from kafka import KafkaProducer
    from kafka.admin import KafkaAdminClient, NewTopic

    logger = logging.getLogger("cot-client-cli")

    args = parse_args()

    admin_client = KafkaAdminClient(
        bootstrap_servers=args.kafka_bootstrap_servers,
        client_id="cot-client-producer",
    )
    topics = ["events"]
    # Check if topics already exist first
    existing_topics = admin_client.list_topics()
    for topic in topics:
        if topic not in existing_topics:
            admin_client.create_topics(
                [NewTopic(topic, num_partitions=1, replication_factor=1)]
            )

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
        process_stocks_task = pgs.add_task("[green]Processing:", total=None)

        if args.historical:
            events = historical_cot_report
        else:
            events = latest_cot_report

        for event in events():
            send_event(event)
            pgs.advance(process_stocks_task)


if __name__ == "__main__":
    logging.basicConfig(handlers=[RichHandler()], level=logging.ERROR)
    main()
