import os
from bytewax.connectors.kafka import KafkaInput, KafkaOutput
from bytewax.dataflow import Dataflow
from bytewax.window import EventClockConfig, TumblingWindow
from calculator.math import AverageTrueRange, AverageDirectionalIndex, MACD, RSI

BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "localhost:19092").split(",")
KAFKA_INPUT_TOPICS = os.getenv("KAFKA_INPUT_TOPICS", "events").split(",")
KAFKA_OUTPUT_TOPIC = os.getenv("KAFKA_OUTPUT_TOPIC", "features")


def prepare_output_topic():
    from confluent_kafka.admin import AdminClient, NewTopic

    admin_client = AdminClient({"bootstrap.servers": BOOTSTRAP_SERVERS[0]})
    fs = admin_client.create_topics(
        [NewTopic(KAFKA_OUTPUT_TOPIC, num_partitions=1, replication_factor=1)],
        validate_only=False,
    )
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print("Topic {} created".format(topic))
        except Exception as e:
            print("Failed to create topic {}: {}".format(topic, e))


def calculate_features():
    import json
    from datetime import datetime, timedelta, timezone

    prepare_output_topic()

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
        item_v["date"] = datetime.fromisoformat(item_v["date"]).astimezone(timezone.utc)
        return item_v["symbol"], item_v

    flow.map(deserialize)

    flow.collect_window(
        "sort_by_date",
        EventClockConfig(lambda e: e["date"], wait_for_system_duration=timedelta(0)),
        TumblingWindow(
            length=timedelta(days=1),
            align_to=datetime(2023, 7, 17, tzinfo=timezone.utc),
        ),
    )
    flow.map(lambda kv: (kv[0], kv[1][0]))

    AverageTrueRange(p=14)(flow)
    AverageDirectionalIndex(p=14)(flow)
    MACD()(flow)
    RSI()(flow)

    def serialize_with_key(key__payload):
        key, payload = key__payload
        new_key_bytes = key if key else json.dumps("unk_key").encode("utf-8")
        payload["date"] = payload["date"].isoformat()

        return new_key_bytes, json.dumps(payload).encode("utf-8")

    flow.map(serialize_with_key)

    flow.output(
        "features", KafkaOutput(brokers=BOOTSTRAP_SERVERS, topic=KAFKA_OUTPUT_TOPIC)
    )

    return flow
