from pybox.color import *
from pybox.led import LED
from pybox.button import BUTTON
from digitalio import DigitalInOut, Direction, Pull
import board
import time

led = LED("external")
btn = BUTTON()

previous = True

while True:
    current = btn.value
    if current != previous:
        if current:
            led.on()
        else:
            led.off()
        previous = current
