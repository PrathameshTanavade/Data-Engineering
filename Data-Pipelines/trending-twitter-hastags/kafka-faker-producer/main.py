import json
from kafka import KafkaProducer

topic_name="tweet"

producer=KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v:json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii')
        )


from tweets import tweet
import time
from faker import Faker

fake=Faker()
fake.add_provider(tweet)
i=0

while i<100:
    message,key=tweet.produce_msg(
            i,
            fake,
            )
    print("Sending:{}".format(message))

    producer.send(topic_name,
                  key=key,
                  value=message)

    time.sleep(2)

    if(i%100)==0:
        producer.flush()
    i=i+1

producer.flush()
