import meshtastic
from pubsub import pub
import meshtastic.serial_interface
from time import sleep

def onReceive(packet, interface):
    print(packet.get('decoded').get('text'))
    

interface = meshtastic.serial_interface.SerialInterface()

pub.subscribe(onReceive, "meshtastic.receive.text")

while true:
    print("Waiting")
    sleep(10)


userInput = input("Input:")