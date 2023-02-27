import board
import analogio
import time


class POT:
    def __init__(self):
        self._adc = analogio.AnalogIn(board.A0)
        
    @property
    def midivalue(self):
        return self._adc.value >> 9
    
    @property
    def value(self):
        return self.midivalue / 128

if __name__=='__main__':
    pot = POT()
    while True:
        print(f"{pot.value},\t{pot.midivalue}")
        time.sleep(0.1)
