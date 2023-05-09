import json
from kafka import KafkaProducer

folderName="/kafka-faker-datagen/"

producer=KafkaProducer(
        bootstrap_servers="localhost",
        value_serializer=lambda v: json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii')
        )

producer.send("test-topic",
              key={"key":1},
              value={"message":"hello world"}
              )
producer.flush()

