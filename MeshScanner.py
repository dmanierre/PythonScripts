import meshtastic
from pubsub import pub
import meshtastic.serial_interface
from time import sleep

def onReceive():
    global action
    packetText = packet.get("decoded").get("text").upper().split("_")
    if "SCAN" in packetText:
        if "START" in packetText:
            action = "START"
        elif "STOP" in packetText:
            action = "STOP"
    elif "TERMINATE" in packetText:
        action = "TERMINATE"
        

macPattern = "[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9][a-zA-Z0-9]"
helpText = "Commands: \n Start Scan \n Pause Scan \n Stop Scan \n Terminate"
action = ""

interface = meshtastic.serial_interface.SerialInterface()
pub.subscribe(onReceive, "meshtastic.receive.text")
interface.sendText("Scanner Connected")

while action != "TERMINATE":
    while action == "START":
        os.system("sudo tshark -i mon1 -a duration:20 > scanResults.txt")
        macAddresses = set()
        FileHandler = open("scanResults.txt","r")
        for line in FileHandler:
            if "Probe Request" in line:
                if "802.11 228" not in line:
                    if re.search(macPattern, line):
                        tempMac = re.search(macPattern, line).group(0)
                        if tempMac not in macAddresses:
                            macAddresses.add(tempMac)
                
        interface.sendText(len(macAddresses))
        FileHandler.close()
        sleep(.5)
        
    print("Scan Stopped")
    sleep(5)

    
    