from neopixel import NeoPixel
import board
import time
pin = board.GP27
led = NeoPixel(pin, 12, brightness=0.2, auto_write=True)
    
c = 0

"""
while True:
    if c != 0:
        led[(c - 1)%12] = (0,0,0)
    led[c%12] = (0,0,255)
    time.sleep(0.025)
    c += 1
"""

led.fill((0,0,0))