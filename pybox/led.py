"""
*This module help you to manage single rgb led (internal or external).*

---

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
    """Led class.

    Args:
        target (str, optional): led to drive, 'internal', 'external' or a board string (i.e. board.GP18).
        color (tuple[int], optional): color in (r, g, b) format.
        brightness (float, optional): value between 0.0 and 1.0.

    Examples:
        >>> led = LED('external')
        >>> led.color = BLUE
        >>> led.on()
    """

    def __init__(self, target: str = 'internal', color: tuple[int] = RED, brightness: float = 0.25, order: str = 'GRB'):
        if target == 'internal':
            pin = board.GP16
            order = 'RGB'
        elif target == 'external':
            pin = board.GP27
            order = 'RGB'
        else:
            pin = target

        self._np = NeoPixel(
            pin, 1, brightness=brightness, auto_write=True, pixel_order=order)

        self._col = color

    def write(self, value: int, color: tuple = None) -> None:
        """Write digital value on led.

        Examples:
            >>> # turn on the led with color RED
            >>> led.write(1, RED)
            >>> # turn off the led
            >>> led.write(0)

        Args:
            value: value to write: 1 to turn on the led, 0 otherwise
            color: color in tuple (r, g, b) format
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
        """Get or set the color.

        Examples:
            >>> led.color = GREEN
            >>> led.on()

        Returns:
            (tuple): color in tuple format
        """
        return self._col

    @color.setter
    def color(self, col):
        self._col = col

    @property
    def brightness(self) -> float:
        """Get or set the brightness

        Examples:
            >>> # fade in brightness starting from 0 to 1
            >>> import time
            >>> led.on()
            >>> led.brightness = 0
            >>> for i in range(101):
            >>>     led.brightness = i / 100
            >>>     time.sleep(0.01)

        Returns:
            brightness value as a float between 0.0 and 1.0
        """
        return self._np.brightness

    @brightness.setter
    def brightness(self, bright):
        self._np.brightness = bright


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
