import os

from bytewax.connectors.kafka import KafkaInput, KafkaOutput
from bytewax.dataflow import Dataflow

from etl.math import (
    MA,
    MACD,
    MFI,
    RSI,
    AverageDirectionalIndex,
    AverageTrueRange,
    CoppockCurve,
    SwingLow,
)


def prepare_output_topic(bootstrap_servers, kafka_output_topic):
    from confluent_kafka.admin import AdminClient, NewTopic

    admin_client = AdminClient({"bootstrap.servers": bootstrap_servers[0]})
    fs = admin_client.create_topics(
        [NewTopic(kafka_output_topic, num_partitions=1, replication_factor=1)],
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
    from datetime import datetime, timezone

    BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "localhost:19092").split(",")
    KAFKA_INPUT_TOPICS = os.getenv("KAFKA_INPUT_TOPICS", "events").split(",")
    KAFKA_OUTPUT_TOPIC = os.getenv("KAFKA_OUTPUT_TOPIC", "features")

    prepare_output_topic(
        bootstrap_servers=BOOTSTRAP_SERVERS, kafka_output_topic=KAFKA_OUTPUT_TOPIC
    )

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

    AverageTrueRange(p=14)(flow)
    AverageDirectionalIndex(p=14)(flow)
    MACD()(flow)
    RSI()(flow)
    MA(window=50)(flow)
    MA(window=200)(flow)
    MFI()(flow)
    SwingLow()(flow)
    CoppockCurve()(flow)

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
