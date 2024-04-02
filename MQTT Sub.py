import paho.mqtt.client as paho
import json
import chardet

def on_message(mosq, obj, msg):
    encoding = chardet.detect(msg.payload)['encoding']
    dataStr = msg.payload.decode(encoding)

    if dataStr:
        data = json.loads(msg.payload)
        if "payload" in data.keys():
            if "text" in data["payload"].keys():
                message = data['payload']['text']
                print(message)

    else:
        print('Empty: ' + dataStr)
        print(msg.payload)

    mosq.publish('pong', 'ack', 0)

def on_publish(mosq, obj, mid, reason_codes, properties):
    pass


client = paho.Client(paho.CallbackAPIVersion.VERSION2)
client.username_pw_set(username="drone",password="derek")
client.on_message = on_message
client.on_publish = on_publish

client.connect("192.168.12.247", 1883, 60)

client.subscribe("testTopic/2/json/mqtt/!f7249454", 0)

client.loop_start()
while True:
    pass