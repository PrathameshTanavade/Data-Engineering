import json
from kafka import KafkaProducer

topic_name="tweet"

producer=KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v:json.dumps(v).encode('utf-8'),
        key_serializer=lambda v: json.dumps(v).encode('utf-8')
        )


from tweets import tweet
import time
from faker import Faker

fake=Faker()
fake.add_provider(tweet)
i=0

while i<10000:
    message,key=tweet.produce_msg(
            i,
            fake,
            )
    print("Sending:{}".format(message))

    producer.send(topic_name,
                  key=key,
                  value=message)

    time.sleep(0.1)

    if(i%10000)==0:
        producer.flush()
    i=i+1

producer.flush()
