import time
import random
import usb_midi
import adafruit_midi

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

print("Midi test")
print("Default output MIDI channel:", midi.out_channel)

previous_time = time.monotonic_()
m_status = 120

while True:
    #midi.send(NoteOn(60, 120))
    current_t = time.monotonic()
    if (current_t - previous_time) >= 0.1:
        m_status = 120 - m_status
        midi.send(NoteOn(60, m_status))
        previous_time = current_t
        