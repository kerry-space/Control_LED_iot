from machine import Pin

class LEDControl:
    def __init__(self, pin):
        self.led = Pin(pin, Pin.OUT)

    def turn_on(self):
        self.led.value(1)
        print("LED is ON")

    def turn_off(self):
        self.led.value(0)
        print("LED is OFF")

    def get_status(self):
        return self.led.value()  