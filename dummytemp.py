import time
import random
from kafka import KafkaProducer
bootstrap_server = ["localhost:9092"]
topic ="tempreature"
producer = KafkaProducer(bootstrap_servers = bootstrap_server)
producer = KafkaProducer()
def senddata():
    message = producer.send(topic,bytes(data))
    metadata = message.get()
    print(metadata.topic)
    print(metadata.partition)
    time.sleep(5)
while True:
    senddata()