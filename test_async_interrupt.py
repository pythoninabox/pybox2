import asyncio
import board
import keypad

keys = keypad.Keys((board.GP6,), value_when_pressed=False)

def pressed():
    print("pressed")
    
def released():
    print("released")
    
while True:
    event = keys.events.get()
    if event:
        if event.pressed:
            pressed()
        elif event.released:
            released()
    
