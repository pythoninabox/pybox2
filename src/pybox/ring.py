from neopixel import NeoPixel
import board
import time
from collections import namedtuple

# led = NeoPixel(board.GP27, 8, bpp=3, brightness=0.3, auto_write=True)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 150, 0)
CYAN = (0, 255, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)


class RING:
    NUMBER = 12

    def __init__(self, ctrl_pin=board.GP27, color=RED, brightness=0.25):

        # _pin = getattr(board, 'GP'+str(ctrl_pin))

        self._np = NeoPixel(
            ctrl_pin, RING.NUMBER, brightness=brightness, auto_write=True)

        self._col = color

        for i in range(RING.NUMBER):
            self._np[i] = SubTuple(self._np[i])

    def __setitem__(self, index, item):
        self._np[index] = item

    def __getitem__(self, index):
        return self._np[index]


SubTuple = namedtuple('SubTuple', ('item',))


class SubTuple(tuple):
    def __new__(self, item):
        # self.data = item
        return tuple.__new__(SubTuple, (item,))

    def on(self, col=RED):
        self.data = col


"""
class Point(tuple):
...    def __new__(self, x, y):
...        return tuple.__new__(Point, (x, y))
"""

# https://jfine-python-classes.readthedocs.io/en/latest/subclass-tuple.html
