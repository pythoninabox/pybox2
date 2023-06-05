import digitalio, board
import time

led = digitalio.DigitalInOut(board.GP29)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = not led.value
    time.sleep(0.125)