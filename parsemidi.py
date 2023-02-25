#!/usr/bin/env python3

import mido
from mido import MidiFile

path = 'onetrack.MID'
mid = MidiFile(path)

"""
notes = []

for msg in mid:
    if msg.type in ['note_on', 'note_off']:
        notes.append([msg.type, msg.note, msg.time - 0.01125])

for n, note in enumerate(notes):
    if n % 2 == 0:
        timeon = note[2]
        timeoff = notes[n+1][2]
        print(timeoff - timeon)
"""

notes = []

# print(mid.tracks[1])
# print(type(mid.tracks[1]))

for msg in mid.tracks[1]:
    if isinstance(msg, mido.messages.messages.Message):
        if msg.type in ['note_on', 'note_off']:
            notes.append([msg.type, msg.note, msg.time])

for n, note in enumerate(notes):
    if n % 2 == 0:
        # print(f"time.sleep({note[2]})")
        #print(f"note: {note[1]},\tnote duration: {notes[n+1][2]}")
        #singleton = {}
        #singleton['delay'] = note[2]
        #singleton['pitch'] = note[1]
        #singleton['dur'] = notes[n+1][2]
        print([note[2], note[1], notes[n+1][2]], ',')
