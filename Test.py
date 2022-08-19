import re
import os
from time import sleep


sleep(60)
print("Starting Scan")
# To Do: Create scan thread dynamically so it can be started again after being stopped.
# Create a paused input + Loop in the scan thread method to avoid restarting thread
macPattern = "[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9]+:[a-zA-Z0-9][a-zA-Z0-9]"

#10 Second Scan ouput
os.system("sudo tshark -i mon1 -a duration:10 > scanResults.txt")
macAddresses = set()
FileHandler = open("scanResults.txt","r")
OutputFile = open("TenSecondScan.txt","w")
for line in FileHandler:
    if "Probe Request" in line:
        if "802.11 228" not in line:
            if re.search(macPattern, line):
                tempMac = re.search(macPattern, line).group(0)
                if tempMac not in macAddresses:
                    macAddresses.add(tempMac)
                    OutputFile.write(tempMac + "\n")
        
OutputFile.write(str(len(macAddresses)))
FileHandler.close()
OutputFile.close()

#20 Second Scan output
os.system("sudo tshark -i mon1 -a duration:20 > scanResults.txt")
macAddresses = set()
FileHandler = open("scanResults.txt","r")
OutputFile = open("TwentySecondScan.txt","w")
for line in FileHandler:
    if "Probe Request" in line:
        if "802.11 228" not in line:
            if re.search(macPattern, line):
                tempMac = re.search(macPattern, line).group(0)
                if tempMac not in macAddresses:
                    macAddresses.add(tempMac)
                    OutputFile.write(tempMac + "\n")
        
OutputFile.write(str(len(macAddresses)))
FileHandler.close()
OutputFile.close()


#30 Second Scan Output
os.system("sudo tshark -i mon1 -a duration:30 > scanResults.txt")
macAddresses = set()
FileHandler = open("scanResults.txt","r")
OutputFile = open("ThirtySecondScan.txt","w")
for line in FileHandler:
    if "Probe Request" in line:
        if "802.11 228" not in line:
            if re.search(macPattern, line):
                tempMac = re.search(macPattern, line).group(0)
                if tempMac not in macAddresses:
                    macAddresses.add(tempMac)
                    OutputFile.write(tempMac + "\n")
        
OutputFile.write(str(len(macAddresses)))
FileHandler.close()
OutputFile.close()

#60 Second Scan Output
os.system("sudo tshark -i mon1 -a duration:60 > scanResults.txt")
macAddresses = set()
FileHandler = open("scanResults.txt","r")
OutputFile = open("SixtySecondScan.txt","w")
for line in FileHandler:
    if "Probe Request" in line:
        if "802.11 228" not in line:
            if re.search(macPattern, line):
                tempMac = re.search(macPattern, line).group(0)
                if tempMac not in macAddresses:
                    macAddresses.add(tempMac)
                    OutputFile.write(tempMac + "\n")
        
OutputFile.write(str(len(macAddresses)))
FileHandler.close()
OutputFile.close()

print("done")
sleep(5)