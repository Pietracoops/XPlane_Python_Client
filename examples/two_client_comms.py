from XPlaneApi import XPlaneClient
import time

client1 = XPlaneClient("Python1")
client2 = XPlaneClient("Python2")


# Call the connect command
if not client1.connect():
   print("Connection client 1 failed")
   exit()
if not client2.connect():
   print("Connection client 1 failed")
   exit()

# Modify and read value at same time
for i in range(0, 100, 1):
   print(f"{client1.topic} send for dref = {str(i / 100)}")
   if not client1.setDataRef("ipcl/deviation_model/value1", str(i/100), True) == 0:
       print("command did not execute correctly!")

   dataRefVal = client2.getDataRef("ipcl/deviation_model/value1")
   print(f"{client2.topic} received for dref = {dataRefVal}")
   time.sleep(0.005)

#time.sleep(3)

print("terminated")