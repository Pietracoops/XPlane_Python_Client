import atexit
import time

import zmq


class XPlaneClient:

    def __init__(self, topic, ip="127.0.0.1"):

        # Initialize a zeromq context
        self.context = zmq.Context()
        self.ip = ip
        self.topic = topic

        try:
            publisher_port = int(input("Enter the publisher's port (press Enter for default 5556):\n"))
        except ValueError:
            publisher_port = 5556
            
        try:
            subscriber_port = int(input("Enter the subscriber's port (press Enter for default 5555):\n"))
        except ValueError:
            subscriber_port = 5555

        self.subscription_port = subscriber_port
        self.publication_port = publisher_port

        self.sleep_time = 1.0
        
        atexit.register(self.disconnect)

    def connect(self):
        """
        Connect to the C++ client. Make sure that Xplane and the C++ client are running

        """
        
        # Set up a channel to send work
        while (True):
            try:
                self.publisher = self.context.socket(zmq.PUB)
                self.publisher.bind(f"tcp://{self.ip}:{self.publication_port}") # Initialization port

                self.subscriber = self.context.socket(zmq.SUB)
                self.subscriber.connect(f"tcp://{self.ip}:{self.subscription_port}")
                self.subscriber.subscribe(self.topic)
                break
            except:
                # Wait till socket is available
                print("Trying to connect to server")
                time.sleep(self.sleep_time)
                
        # Give everything a second to spin up and connect
        time.sleep(self.sleep_time)

        # Send initial connection string to register to server
        self.publisher.send_multipart([bytes(self.topic, 'utf-8'), b"Connection"])
        time.sleep(self.sleep_time)
        
        response = self.subscriber.recv_multipart()
        
        # Disconnect and unbind from old sockets
        self.publisher.unbind(f"tcp://{self.ip}:{self.publication_port}")
        self.subscriber.disconnect(f"tcp://{self.ip}:{self.subscription_port}")
        
        self.publication_port = response[1].decode("utf-8")
        self.subscription_port = response[2].decode("utf-8")
        print(f"Connected to Xplane Server on publication {self.publication_port} port and subscription {self.subscription_port} port")

        # Rebind the connection for the new ports
        self.publisher.bind(f"tcp://{self.ip}:{self.publication_port}")
        self.subscriber.connect(f"tcp://{self.ip}:{self.subscription_port}")

        # Give everything a second to spin up and connect
        time.sleep(self.sleep_time)

    def disconnect(self):
        # Send disconnection message to server
        self.publisher.send_multipart([bytes(self.topic, 'utf-8'), b"Disconnection", b"0", b"0"])
        response = self.subscriber.recv_multipart()

        print("Client disconnected")
        if "Received" in response[1].decode("utf-8"):
            self.subscriber.disconnect(f"tcp://{self.ip}:{self.subscription_port}")
            self.publisher.unbind(f"tcp://{self.ip}:{self.publication_port}")
            return True
        else:
            return False


    def getDataRef(self, dref):
        """
        Get the value of a dataref as a string.

        Args:
            response (set): dataRef of interest as a string, time elasped since last update of dataref in seconds

        Returns:
            str: Value of the dataRef
        """
        self.publisher.send_multipart([bytes(self.topic, 'utf-8'), b"read", bytes(dref, 'utf-8'), b"0"])
        response = self.subscriber.recv_multipart()
        return response[1].decode("utf-8"), response[2].decode("utf-8")

    def setDataRef(self, dref, value, verbose=False):
        """
        Set the dataref to the specified value.

        Args:
            dref (str): Dataref of interest
            value (str): Value of the dataref

        Returns:
            bool: True of successfully sent, false otherwise.
        """
        self.publisher.send_multipart([bytes(self.topic, 'utf-8'), b"set", bytes(dref, 'utf-8'), bytes(value, 'utf-8')])
        response = self.subscriber.recv_multipart()
        response_message = response[1].decode("utf-8")
        
        if verbose:
            print(response_message)
        
        if "Received" in response_message:
            return 0
        elif "Error" in response_message:
            return 1
        else:
            return 2
            
    def terminate(self, verbose=False):
        """
        Liberate position of writer

        Returns:
            bool: True of successfully sent, false otherwise.
        """
        self.publisher.send_multipart([bytes(self.topic, 'utf-8'), b"terminate", b"0", b"0"])
        response = self.subscriber.recv_multipart()
        response_message = response[1].decode("utf-8")
        
        if verbose:
            print(response_message)
        
        if "Received" in response_message:
            return 0
        elif "Error" in response_message:
            return 1
        else:
            return 2

    def sendCommand(self, dref, verbose=False):
        """
        Send command to Xplane.

        Args:
            dref (str): Designated command to be sent

        Returns:
            bool: True of successfully sent, false otherwise.
        """
        self.publisher.send_multipart([bytes(self.topic, 'utf-8'), b"command", bytes(dref, 'utf-8'), b"0"])
        response = self.subscriber.recv_multipart()
        
        if "Received" in response[1].decode("utf-8"):
            return 0
        else:
            return 1


