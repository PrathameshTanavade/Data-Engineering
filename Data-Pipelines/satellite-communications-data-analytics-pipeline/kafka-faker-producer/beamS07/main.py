import json
from kafka import KafkaProducer

folderName="/kafka-faker-sat-comm-datagen/"
topic_name="sat-comm"

producer=KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v:json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii')
        )


from beamS07 import BeamS07
import time
from faker import Faker

fake=Faker()
fake.add_provider(BeamS07)
i=0

while i<100:
    message,key=BeamS07.produce_msg(
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
