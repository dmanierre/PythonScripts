import paho.mqtt.client as mqtt
from random import uniform
import time
import json

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username="drone",password="derek")
client.connect('192.168.12.247')

message = {
    "from":4146369620,
    "channel":0,
    "type":"sendtext",
    "payload": "mqtt-test"
}

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("testTopic/2/json/mqtt", payload=json.dumps(message))
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(10)

    http://www.steves-internet-guide.com/client-connections-python-mqtt/