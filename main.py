import atexit
import time

from XPlaneApi.XPlaneAPI import XPlaneClient

def disconnect():
    client.disconnect()

# Specify a topic for your program to communicate through
# Specify also as input IP address of pc containing xplane if not local

name = input("Enter the topic of the python client (default Python Client):\n") or "Python Client"

client = XPlaneClient(name)

# Call the connect command
client.connect()

# Modify and read value at same time
for i in range(0, 100, 1):
    if client.setDataRef("sim/cockpit2/engine/actuators/throttle_ratio[0]", str(i/100)) == False:
        print("Command did not execute correctly!")

    dataRefVal = client.getDataRef("sim/cockpit2/engine/actuators/throttle_ratio[0]")
    print(f"Value received for dref = {dataRefVal}")
    time.sleep(0.005)

atexit.register(disconnect)