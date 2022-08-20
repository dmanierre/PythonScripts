from ast import arg
import re
import os
import threading
from time import sleep
from pubsub import pub
import meshtastic

def onReceive(packet, interface):
    global action
    packetText = packet.get('decoded').get('text').upper().split("_")
    if "SCAN" in packetText:
        if "START" in packetText:
            action = "START"
        elif "STOP" in packetText:
            action = "STOP"
    elif "TERMINATE" in packetText:
        action = "TERMINATE"

# To Do: Create scan thread dynamically so it can be started again after being stopped.
# Create a paused input + Loop in the scan thread method to avoid restarting thread
macPattern = "[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9][a-zA-Z0-9]"
helpText = "Commands: \n Start Scan \n Pause Scan \n Stop Scan \n Terminate"
runScan = ""
action = ""
scanTime = 20 #Default to 20 seconds


interface = meshtastic.serial_interface.SerialInterface()
pub.subscribe(onReceive, "meshtastic.receive.text")
interface.sendText("Scanner Connected")


while action != "TERMINATE":
    while(runScan == "Run" or runScan == "Pause"):
            while(runScan == "Pause"):
                print("Scan Paused")
                #call method to check if action has been updated
            os.system("sudo tshark -i mon1 -a duration:20 > scanResults.txt")
            macAddresses = set()
            FileHandler = open("scanResults.txt","r")
            for line in FileHandler:
                if "Probe Request" in line:
                    if "802.11 228" not in line:
                        if re.search(macPattern, line):
                            tempMac = re.search(macPattern, line).group(0)
                            if tempMac not in macAddresses:
                                print("Address Added: " + tempMac)
                                macAddresses.add(tempMac)
                    
            print(len(macAddresses))
            interface.sendText("Devices Found: " + len(macAddresses))
            FileHandler.close()
            #call method to check if action has been updated
            sleep(.5)

    



def inputLoop():
    interface = meshtastic.serial_interface.SerialInterface()
    pub.subscribe(onReceive, "meshtastic.receive.text")
    interface.sendText("Scanner Connected")
    global input
    global runScan
    while userInput.upper() != 'TERMINATE':
        userInput = input("Input:")
        if userInput.upper() == "START SCAN":
            runScan = "Run"
        elif userInput.upper() == "PAUSE SCAN":
            runScan = "Pause"
        elif userInput.upper() == "HELP":
            print(helpText)
        elif userInput.upper() == "STOP SCAN":
            runScan = "Stop"
    
    runScan = "Stop"
    print("Finishing")
    sleep(5)


sLoop = threading.Thread(name="scanLoop", target=scanLoop)
iLoop = threading.Thread(name="inputLoop", target=inputLoop)


iLoop.start()
sLoop.start()