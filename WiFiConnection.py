import network
import time

class WiFiConnection:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self):
        self.wlan.active(True)
        self.wlan.disconnect()
        print(f"Connecting to {self.ssid}...")
        self.wlan.connect(self.ssid, self.password)

        # Wait for connection
        while not self.wlan.isconnected():
            print("Waiting for connection...")
            time.sleep(1)
        
        print(f"Connected to {self.ssid} with IP {self.wlan.ifconfig()[0]}")

    def disconnect(self):
        if self.wlan.isconnected():
            self.wlan.disconnect()
            self.wlan.active(False)
            print("Disconnected from WiFi.")