import board
from neopixel import NeoPixel
import time
import random

RED = (0, 255, 0)
GREEN = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (150, 255, 0)
CYAN = (255, 0, 255)
PURPLE = (0, 180, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)


class LED:
    REF = None

    def __init__(self, color=RED, brightness=0.3):

        if LED.REF:
            LED.REF.deinit()

        self._np = NeoPixel(
            board.GP16, 1, brightness=brightness, auto_write=True)

        self._col = color
        LED.REF = self._np

    def write(self, value, color=None):
        """write digital value on led"""
        if value:
            if color:
                self._col = color
            value = self._col

        else:
            value = OFF

        self._np[0] = value
        # self._np.write()

    def on(self):
        self.write(1)

    def off(self):
        self.write(0)

    def toggle(self):
        if self._np[0] == (0, 0, 0):
            self.write(1)
        else:
            self.write(0)

    @property
    def color(self):
        return self._col

    @color.setter
    def color(self, col):
        self._col = col

    @property
    def brightness(self):
        return self._np.brightness

    @brightness.setter
    def brightness(self, br):
        self._np.brightness = br


if __name__ == '__main__':
    led = LED(16, GREEN)
    colori = [RED, GREEN, BLUE]

    def test(t):
        while True:
            led.digital_write(1, colori[random.randint(0, 2)])
            time.sleep(t)
            led.digital_write(0)
            time.sleep(t)

    test(0.125)
