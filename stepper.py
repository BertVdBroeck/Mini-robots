from machine import Pin
from time import sleep_ms

class Stepper:

    def __init__(self, pins):
        self.poles = []
        for pin in pins:
            self.poles.append(Pin(pin, Pin.OUT, value=0))
        self.steps = 0


    def update_poles(self):
        rest = self.steps % 4
        for i in range(4):
            if rest == i:
                self.poles[i].high()
            else:
                self.poles[i].low()

    def forward(self):
        self.steps = self.steps + 1
        self.update_poles()

    def backward(self):
        self.steps = self.steps - 1
        self.update_poles()



stepper_right = Stepper([16, 5, 4, 0])
stepper_left = Stepper([14, 12, 13, 15])

while True:
    for i in range(513 * 4):
        stepper_right.forward()
        stepper_left.backward()
        sleep_ms(1)

    for i in range(513 * 4):
        stepper_right.backward()
        stepper_left.forward()
        sleep_ms(1)
