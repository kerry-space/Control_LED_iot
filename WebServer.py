import socket
import json

class WebServer:
    def __init__(self, led_control):
        self.led_control = led_control
        self.address = ('', 80)  # Port 80 for HTTP

    def start_server(self):
        # Create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(self.address)
        s.listen(1)
        print("Web server started, listening on port 80...")

        while True:
            # Accept client connection
            conn, addr = s.accept()
            print(f"Connection from {addr}")
            request = conn.recv(1024).decode()
            print(f"Request: {request}")

            # Check request type
            if "/api/led" in request:
                # Respond with LED status in JSON
                self.send_json_response(conn)
            elif "/?led=on" in request:
                # Turn on the LED
                self.led_control.turn_on()
                self.send_html_response(conn)
            elif "/?led=off" in request:
                # Turn off the LED
                self.led_control.turn_off()
                self.send_html_response(conn)
            else:
                # Serve the HTML page
                self.send_html_response(conn)

            conn.close()

    def send_html_response(self, conn):
        # Get the current state of the LED
        gpio_state = "ON" if self.led_control.get_status() else "OFF"
        
        # Updated HTML with dynamic GPIO state
        html = """
        <html>
            <head>
                <title>Pico W Web Server</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="icon" href="data:,">
                <style>
                    html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
                    h1{color: #0F3376; padding: 2vh;}
                    p{font-size: 1.5rem;}
                    button{display: inline-block; background-color: #4286f4; border: none; border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
                    .button2{background-color: #4286f4;}
                </style>
            </head>
            <body> 
                <h1>Pico W Web Server</h1> 
                <p>GPIO state: <strong>""" + gpio_state + """</strong></p>
                <p><a href="/?led=on"><button class="button">ON</button></a></p>
                <p><a href="/?led=off"><button class="button button2">OFF</button></a></p>
            </body>
        </html>
        """
        
        # Send the response
        response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n" + html
        conn.send(response.encode())

    def send_json_response(self, conn):
        led_status = "on" if self.led_control.get_status() else "off"
        json_data = {"led_status": led_status}
        response = "HTTP/1.1 200 OK\nContent-Type: application/json\n\n" + json.dumps(json_data)
        conn.send(response.encode())