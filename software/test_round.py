from pybox.pot import POT
from pybox.button import BUTTON
from pybox.tone import TONE
from pybox.ring import RING
from pybox.color import *
import time


pot = POT()
but = BUTTON()
tone = TONE()
ring = RING()

for i in range(12):
    ring.fill(0)
    ring[i] = RED
    tone.mplay(i + 60, 0.125)
    
ring.fill(0)


while True:
    print("POT:", pot.value, "BUTTON:", but.value)
    time.sleep(0.1)
