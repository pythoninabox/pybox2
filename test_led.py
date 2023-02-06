import board
from neopixel import NeoPixel
import time
import random

RED = (0, 255, 0)
GREEN = (255, 0, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)


class LED:
    RED = (0, 255, 0)
    OFF = (0, 0, 0)

    def __init__(self, pin=None, col=RED, brightness=0.3):
        self._brightness = brightness
        try:
            self._np = NeoPixel(
                board.GP16, 1, brightness=brightness, auto_write=True)
        except ValueError:
            self._np.deinit()
            self._np = NeoPixel(
                board.GP16, 1, brightness=brightness, auto_write=True)

        self._col = col

    def digital_write(self, value, color=None):
        if value:
            if color:
                self._col = color
            value = self._col

        else:
            value = OFF

        self._np[0] = value
        # self._np.write()

    @property
    def color(self):
        return self._col

    @color.setter
    def color(col):
        self._col = col

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(br):
        self._brightness = br


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
