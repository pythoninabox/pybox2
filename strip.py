from neopixel import NeoPixel
import board
import time

# led = NeoPixel(board.GP27, 8, bpp=3, brightness=0.3, auto_write=True)
RED = (0, 255, 0)
GREEN = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (150, 255, 0)
CYAN = (255, 0, 255)
PURPLE = (0, 180, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)


class PixelStrip:
    REF = None
    PIXEL_NUMBER = 8

    def __init__(self, ctrl_pin=14, color=RED, brightness=0.3):

        self._check_busy()

        _pin = getattr(board, 'GP'+str(ctrl_pin))

        self._np = NeoPixel(
            _pin, PixelStrip.PIXEL_NUMBER, brightness=brightness, auto_write=True)

        self._col = color
        PixelStrip.REF = self._np

    """
    def __setitem__(self, index, item):
        self._np[index] = item
        
    def __getitem__(self, index):
        return self._np[index]
    """

    def on(self, index=None):
        if index is not None:
            self._np[index] = self._col
        else:
            self._np.fill(self._col)

    def off(self, index=None):
        if index is not None:
            self._np[index] = OFF
        else:
            self._np.fill(OFF)

    def get_brightness(self, index):
        return self._np[index].brightness

    def set_brightness(self, index, value):
        self._np[index].brightness = value

    def _check_busy(self):
        if PixelStrip.REF:
            PixelStrip.REF.deinit()


led = PixelStrip()

"""
while True:
    for i in range(8):
        if i == 0:
            led.off(7)
        else:
            led.off(i-1)
        
        led.on(i)
        time.sleep(0.1)
"""

led.on(0)
led.on(4)
time.sleep(2)
led._np[0] = tuple(map(lambda x: int(x * 0.75), (0, 255, 0)))
time.sleep(2)
led._np[0] = tuple(map(lambda x: int(x * 0.3), (0, 255, 0)))
time.sleep(2)
led.off(0)
led.off(4)
