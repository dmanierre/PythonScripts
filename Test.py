from time import sleep
import os

print("Copying Old File")

FileHandler = open("scanResults.txt","r")
OutputFile = open("oldSCanResults.txt","w")
for line in FileHandler:
    OutputFile.write(line)

FileHandler.close()
OutputFile.close()

print("File Copied")

print("Getting Packets")

os.system("sudo tshark -i mon1 -a duration:5 > scanResults.txt")

print("Packets Retrieved")
sleep(20)