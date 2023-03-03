import time
import rp2pio
import board
import adafruit_pioasm
from umidi import umidiparser as umid

path = 'courante2_t0.mid'
data = umid.MidiFile(path)

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
        time.sleep(command.delta_us / 1000000)
        if command.velocity == 0:
            sm.stop()
        else:
            sm.restart()
            sm.frequency = mtof(command.note) * 32