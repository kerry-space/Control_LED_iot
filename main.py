from WiFiConnection import WiFiConnection  
from LEDControl import LEDControl
from WebServer import WebServer

# Initialize Wi-Fi, LED control, and web server
wifi = WiFiConnection("Jalal", "jalal123")
led = LEDControl(led)  # GPIO pin 25 for the internal LED
server = WebServer(led)

try:
    wifi.connect()
    server.start_server()
except Exception as e:
    print("Exception:", e)
finally:
    wifi.disconnect()