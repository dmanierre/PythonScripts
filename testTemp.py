import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc, properties):
    if rc==0:
        client.connected_flag = True
        print("Connected")
    else:
        print("Bad connection returned code: ", rc)
        print("Connection Failed")

def on_message(client, userdata, message):
    print("Message: ", str(message.payload.decode("utf-8")))

mqtt.Client.connected_flag = False
broker = '192.168.12.247'

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Test Subscriber")
client.username_pw_set(username="drone",password="derek")
client.on_connect = on_connect
client.loop_start()
print("Trying to Connect to Broker")
try:
    client.connect(broker)
except:
    print("Connection Failed")
    exit(1)


while not client.connected_flag:
    print("Waiting for Conection")
    time.sleep(1)

print("Connection attempt finished")

while True:
    client.subscribe("testTopic")
    client.on_message = on_message
