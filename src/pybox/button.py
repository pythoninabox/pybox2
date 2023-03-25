"""Button manager.

This module help you to manage integrated button.

Examples:
    >>> from pybox.button import BUTTON
    >>> but = BUTTON()
    >>> but.value
    0
    >>> # press and hold the button
    >>> but.value
    1

The user basically should use only the `BUTTON` class inside it.  
"""

import time
import board
from digitalio import DigitalInOut, Direction, Pull

class BUTTON:
    """Button manager.

    Args:
        None
    """
    def __init__(self):
        self.btn = DigitalInOut(board.GP6)
        self.btn.direction = Direction.INPUT
        self.btn.pull = Pull.UP
        self.previous_status = True
        self._actions = []
        self.press_function = None
        self.release_function = None
        
    def update(self):
        """Update button state on main loop.

        Args:
            None
        """
        for func in self._actions:
            func()
        
        self.previous_status = self.btn.value
        
    def press_handler(self, func):
        """Add a function to call when button is pressed.

        Examples:
            >>> def when_pressed():
                    print("PRESSED")
            >>> push = BUTTON()
            >>> push.press_handler(when_pressed)
            >>> while True:
                    push.update()
                    # it prints PRESSED on press button

        Args:
            func (callable): a func to be executed when button is pressed. 

        Todo:
            - Add possibility to add arguments to func
        """
        self.press_function = func
        self._add_handler(self.__pressed)
    
    def release_handler(self, func):
        """Add a function to call when button is released.

        Examples:
            >>> def when_released():
                    print("RELEASED")
            >>> push = BUTTON()
            >>> push.release_handler(when_released)
            >>> while True:
                    push.update()
                    # it prints RELEASED on release button

        Args:
            func (callable): a func to be executed when button is released. 

        Todo:
            - Add possibility to add arguments to func
        """
        self.release_function = func
        self._add_handler(self.__released)
        
    def __pressed(self):
        if not self.btn.value:
            if self.previous_status != self.btn.value:
                self.press_function()
        
    def __released(self):
        if self.btn.value:
            if self.previous_status != self.btn.value:
                self.release_function()
                
    def _add_handler(self, f):
        self._actions.append(f)
        
    @property
    def value(self):
        """Raw button value.

        Returns:
            value (int): button value, 1 if pressed, 0 otherwise
        """
        return int(not self.btn.value)


def pre():
    print("PRESSEEEED :-D")
    
def rel():
    print("__RELEASED :-(")
        
if __name__=='__main__':
        
    push = BUTTON()
    push.press_handler(pre)
    push.release_handler(rel)
    
    while True:
        print(push.value)
        time.sleep(0.1)