from ast import arg
import re
import os
import threading
from time import sleep

def scanLoop():
    global runScan
    while(runScan == "Run" or runScan == "Pause"):
        while(runScan == "Pause"):
            print("Scan Paused")
            sleep(5)
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
        FileHandler.close()
        sleep(.5)

    print("Ending Scan")
    return

def inputLoop():
    userInput = ''
    global runScan
    while userInput.upper() != 'TERMINATE':
        userInput = input("Input:")
        if userInput.upper() == "START SCAN":
            runScan = "Run"
        elif userInput.upper() == "PAUSE SCAN":
            runScan = "Pause"
        elif userInput.upper() == "STOP SCAN":
            runScan = "Stop"
    
    print("Finishing")
    sleep(5)


# To Do: Create scan thread dynamically so it can be started again after being stopped.
# Create a paused input + Loop in the scan thread method to avoid restarting thread
macPattern = "[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9][a-zA-Z0-9]"
runScan = "Pause"

sLoop = threading.Thread(name="scanLoop", target=scanLoop)
iLoop = threading.Thread(name="inputLoop", target=inputLoop)


iLoop.start()
sLoop.start()