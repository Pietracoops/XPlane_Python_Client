import time

from XPlaneApi.XPlaneAPI import XPlaneClient

# Specify a topic for your program to communicate through
# Specify also as input IP address of pc containing xplane if not local
name = input("Enter the topic of the python client (default Python Client):\n") or "Python Client"

client = XPlaneClient(name)

# Call the connect command
client.connect()

# Modify and read value at same time
i = 0
while (i < 100):
    if not client.setDataRef("sim/cockpit2/engine/actuators/throttle_ratio[0]", str(i/100), True) == 0:
        i = 0
        continue
    
    dataRefVal = client.getDataRef("sim/cockpit2/engine/actuators/throttle_ratio[0]")
    print(f"Value received for dref: {dataRefVal}")
    
    i += 0.1
    time.sleep(0.005)

# Free writer spot for other clients    
client.terminate(True)

# Check for non-existant data ref
client.setDataRef("massimo", str(9000), True)

dataRefVal, timeElasped = client.getDataRef("massimo")
print(f"Value received for dref: {dataRefVal}")

# Check for time elsaped since last dataref update
time.sleep(1.0)

dataRefVal = client.getDataRef("sim/cockpit2/engine/actuators/throttle_ratio[0]")
print(f"Value received for dref: {dataRefVal}")
