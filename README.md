# XPlane Python Client

This repository contains a Python client to send commands directly to XPlane through the C++ server.

## Setup
All that is required is to pip install the package.

```
pip install XPlaneApi
```

Then we can import it into a project as follows:

```
from XPlaneApi import XPlaneClient
```

## Running the Setup

* Start XPlane and wait until a flight has been resumed and you are in the aircraft
* Navigate to the folder containing the C++ Server for Xplane
	* Modify the subscriptions.txt to add or remove datarefs that you wish to subscribe to.
	* Execute the libXplane-udp-client.exe when ready
* Begin the Python Client as required

## Python API Documentation

The Python API currently has 3 functions available to use as follows:

Connect to the C++ Server by using the connect function seen below.

```
connect(self):
```

Disconnect cleanly from the C++ Server by using the connect function seen below.

```
disconnect(self):
```

To receive the value of a dataref, use the getDataRef function to receive the value as a string.

```
getDataRef(self, dref):
```

To modify the value of a dataref, use the setDataRef function to alter the value. Note, value must be in string format.

```
setDataRef(self, dref, value):
```

To send a command to the cockpit, use the sendCommand, input must be in the string format.

```
sendCommand(self, dref):
```

## Example Program

This example program comes bundled in the package under examples.

```
from XPlaneApi import XPlaneClient
import time

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
```