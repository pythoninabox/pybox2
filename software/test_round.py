from pybox.ring import RING
from pybox.color import *
from pybox.tone import TONE
import time
import random

ring = RING()
tone = TONE()

for i in range(96):
    ring.set_color(i % 12, get_random_color())
    ring[i % 12] = 1
    note = random.randint(48, 83);
    #tone.mplay(note, 0.1)
    #ring[(i-4) % 12] = 0
    #time.sleep(0.025)
    #tone.mplay(note, 0.1)
    ring.fill(0)
    
ring.fill(0)
