from XPlaneApi import XPlaneClient
import time

def test_xplaneapi():
    # Specify a topic for your program to communicate through
    # Specify also as input IP address of pc containing xplane if not local
    client = XPlaneClient("Python1")

    # Call the connect command
    client.connect()

    # Modify and read value at same time
    for i in range(0, 100, 1):
        if client.setDataRef("sim/cockpit2/engine/actuators/throttle_ratio[0]", str(i/100)) == False:
            print("command did not execute correctly!")

        dataRefVal = client.getDataRef("sim/cockpit2/engine/actuators/throttle_ratio[0]")
        print(f"Value received for dref = {dataRefVal}")
        time.sleep(0.005)

    # Disconnect the client cleanly
    client.disconnect()


test_xplaneapi()