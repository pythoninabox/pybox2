"""Led manager.

This module help you to manage single rgb led (internal or external).

Examples:
    >>> from pybox.led import LED
    >>> from pybox.color import *
    # drive internal led
    >>> led = LED()
    >>> led.color = BLUE
    # turn on the led
    >>> led.on()
    # turn off the led
    >>> led.off()
    
The user basically should use only the `LED` class inside it.  
"""

import board
from neopixel import NeoPixel
import time
import random
from pybox.color import *


class LED:
    """Led manager.
    """
    def __init__(self, target='internal', color=RED, brightness=0.25):

        if target == 'internal':
            pin = board.GP16
            order = 'GRB'
        elif target == 'external':
            pin = board.GP27
            order = 'GRB'

        self._np = NeoPixel(
            pin, 1, brightness=brightness, auto_write=True, pixel_order=order)

        self._col = color

    def write(self, value, color=None):
        """Write digital value on led.
        
        Examples:
            >>> # turn on the led with color RED
            >>> led.write(1, RED)
            >>> # turn off the led
            >>> led.write(0)

        Args:
            value (int): value to write: 1 to turn on the led, 0 otherwise
            color (tuple): color in tuple (r, g, b) format
        """
        if value == 1:
            if color:
                self._col = color

            value = self._col

        else:
            value = OFF

        # print(self._col)
        self._np[0] = value

    def on(self):
        """turn on the led
        """
        self.write(1)

    def off(self):
        """turn off the led
        """
        self.write(0)

    def toggle(self):
        """switch between on and off on the led.

        Examples:
            >>> led.on()
            >>> # turn off the led
            >>> led.toggle()
            >>> # turn on
            >>> led.toggle()
        """

        if self._np[0] == (0, 0, 0):
            self.write(1)
        else:
            self.write(0)

    def deinit(self):
        """deinitialize led.
        """
        self._np.deinit()

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
            led.write(1, colori[random.randint(0, 2)])
            time.sleep(t)
            led.write(0)
            time.sleep(t)

    test(0.125)
