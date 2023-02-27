import time
import board
from digitalio import DigitalInOut, Direction, Pull

class BUTTON:
    def __init__(self):
        self.btn = DigitalInOut(board.GP6)
        self.btn.direction = Direction.INPUT
        self.btn.pull = Pull.UP
        self.previous_status = True
        self._actions = []
        
    def update(self):
        for func in self._actions:
            func()
        
        self.previous_status = self.btn.value
        
    def press_handler(self, func):
        self.press_function = func
        self._add_handler(self.pressed)
    
    def release_handler(self, func):
        self.release_function = func
        self._add_handler(self.released)
        
    def pressed(self):
        if not self.btn.value:
            if self.previous_status != self.btn.value:
                self.press_function()
        
    def released(self):
        if self.btn.value:
            if self.previous_status != self.btn.value:
                self.release_function()
                
    def _add_handler(self, f):
        self._actions.append(f)
        
    @property
    def value(self):
        return int(not self.btn.value)


def pre():
    print("PRESSEEEED :-D")
    
def rel():
    print("RELEASED :-(")
        
if __name__=='__main__':
        
    push = BUTTON()
    push.press_handler(pre)
    push.release_handler(rel)
    
    while True:
        print(push.value)
        time.sleep(0.1)