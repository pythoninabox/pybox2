from neopixel import NeoPixel
from pybox.color import *
import board, time

led = NeoPixel(board.GP27, 12, brightness=0.25, auto_write=True)
