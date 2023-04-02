import time
import random
import usb_midi
import adafruit_midi

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

class MIDI:
    def __init__(self, channel=0):
        self._midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=channel)

    #midi.send(NoteOn(60, m_status))
    def note_on(self, pitch=60, velocity=100):
        self._midi.send(NoteOn(pitch, velocity))

    def note_off(self, pitch=60):
        self._midi.send(NoteOff(pitch, 0))