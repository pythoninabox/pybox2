import time, random
import rp2pio
import board
import adafruit_pioasm
from umidi import umidiparser as umid
from pybox.ring import RING
from pybox.color import *

path = 'track.mid'
data = umid.MidiFile(path)
ring = RING()
counter = 0

def mtof(m):
    return int(2**((m - 69) / 12) * 440)

squarewave = """
.program squarewave
    set pins 1 [31]    ; Drive pin high and then delay for one cycle
    set pins 0 [31]     ; Drive pin low
"""

assembled = adafruit_pioasm.assemble(squarewave)

sm = rp2pio.StateMachine(
    assembled,
    frequency=1000 * 2,
    first_set_pin=board.GP8,
)
sm.stop()

parsed = []

for command in data:
    if command._get_event_name() == 'note_on':
        time.sleep(command.delta_us / 3000000)
        if command.velocity == 0:
            sm.stop()
            ring.fill(OFF)
        else:
            sm.restart()
            sm.frequency = mtof(command.note + 12) * 32
            ring[command.note % 12] = BLUE