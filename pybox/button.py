"""This module help you to manage integrated button.

Examples:
    >>> from pybox.button import SIMPLEBUTTON
    >>> but = SIMPLEBUTTON()
    >>> but.value
    0
    >>> # press and hold the button
    >>> but.value
    1

The user basically should use only the `BUTTON` class inside it.  
The module consists basically in two class:  
    - `SIMPLEBUTTON`: to retrieve the value of the button  
    - `BUTTON`: to bind custom functions to button behavior
"""

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import keypad


class BUTTON:
    """Button class.
    """
    def __init__(self):
        self.keys = keypad.Keys((board.GP6,), value_when_pressed=False)
        self.press_function = None
        self.release_function = None
        self._press_time = None
        self._press_timestamp = None
        
    def update(self):
        """Update button state on main loop.
        """

        event = self.keys.events.get()
        if event:
            if event.pressed:
                self._press_timestamp = time.monotonic()
                self.press_function()
            elif event.released:
                self._press_time = time.monotonic() - self._press_timestamp
                self.release_function()
        
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

    @property
    def press_time(self):
        """Get time of pressure.

        Returns:
            float: time in float format
        """
        return self._press_time


class SIMPLEBUTTON:
    """SimpleButton class.
    """
    def __init__(self):
        self.btn = DigitalInOut(board.GP6)
        self.btn.direction = Direction.INPUT
        self.btn.pull = Pull.UP

    @property
    def value(self):
        """Raw button value.

        Returns:
            (int): button value, 1 if pressed, 0 otherwise
        """
        return int(not self.btn.value)
        
if __name__=='__main__':
        
    push = BUTTON()
    
    def pre():
        print("PRESSEEEED :-D")
    
    def rel():
        print("__RELEASED :-(")
    
    push.press_handler(pre)
    push.release_handler(rel)
    
    while True:
        push.update()
        #time.sleep(0.001)