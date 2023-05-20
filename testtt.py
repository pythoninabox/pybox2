from pybox.led import LED
from pybox.color import *
import time

led = LED(order='RGB')
led.color = GREEN

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
