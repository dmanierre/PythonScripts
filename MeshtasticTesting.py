import meshtastic
from pubsub import pub
import meshtastic.serial_interface

def onReceive(packet, interface):
    print(packet.get('decoded').get('text'))
    
    interface.sendText("Got It")

interface = meshtastic.serial_interface.SerialInterface()

pub.subscribe(onReceive, "meshtastic.receive.text")


userInput = input("Input:")