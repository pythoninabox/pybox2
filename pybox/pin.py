"""
*This module help you to manage a pin*

---

Examples:
    >>> from pybox.pin import PIN
    >>> led = PIN(9, 'OUTPUT')
    >>> led.value = 1
    
The user basically should use only the `PIN` class inside it.  
"""

import board
import digitalio


class PIN:
    """PIN class

    Args:
        pin (int): pin to drive
        direction (str): `INPUT` or `OUTPUT`
    """

    def __init__(self, pin: int = None, direction: str = None):
        n_pin = getattr(board, f'GP{pin}')
        self._pin = digitalio.DigitalInOut(n_pin)

        if direction in ['INPUT', 'OUTPUT']:
            _dir = getattr(digitalio.Direction, direction)
            self._pin.direction = _dir
        else:
            raise ValueError(
                "Please choose one of the following options: 'INPUT','OUTPUT'")

        self._value = 0

    @property
    def value(self):
        """Get or set pin value

        Returns:
            (int): 0 for null voltage (GND), 1 for maximum voltage (3V3)
        """
        return 1 if self._pin.value else 0

    @value.setter
    def value(self, val: int = 0):
        self._pin.value = bool(val)
