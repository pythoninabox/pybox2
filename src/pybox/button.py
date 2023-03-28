from pybox.led import LED
from pybox.button import BUTTON
import time

push = BUTTON()
led = LED("external")

def pre():
    #print("PRESSEEEED :-D")
    led.on()

def rel():
    #print("RELEASED :-(")
    #print("time of pressure:", push.time_pressed)
    led.off()

push.press_handler(pre)
push.release_handler(rel) 

while True:
    push.update()
    time.sleep(0.001)
