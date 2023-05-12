import json
from kafka import KafkaProducer


folderName="/kafka-faker-datagen/"
topic_name="kafka-faker-pizza"

producer=KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii')
        )


from pizzaproducer import PizzaProvider
import time
from faker import Faker

MAX_NUMBER_PIZZAS_IN_ORDER=10
MAX_ADDITIONAL_TOPPINGS_IN_PIZZA=5



fake=Faker()
fake.add_provider(PizzaProvider)
i=0
while i <  100:
    message, key = PizzaProvider.produce_msg(
            i,
            fake,
            MAX_NUMBER_PIZZAS_IN_ORDER,
            MAX_ADDITIONAL_TOPPINGS_IN_PIZZA,)

    print("Sending: {}".format(message))
    # sending the message to Kafka
    producer.send(topic_name,
                  key=key,
                  value=message)
    # 2 seconds of sleep time before the next message
    time.sleep(2)

    # Force sending of all messages
    if (i % 100) == 0:
        producer.flush()
    i=i+1
producer.flush()
