import board
import digitalio


class PIN:
    def __init__(self, pin: int = None, direction: str = None):
        n_pin = getattr(board, f'GP{pin}')
        self._pin = digitalio.DigitalInOut(n_pin)

        if direction in ['INPUT', 'OUTPUT']:
            _dir = getattr(digitalio.Direction, direction)
            self._pin.direction = _dir
        else:
            raise Exception(
                "Please choose one of the following options: 'INPUT','OUTPUT'")

        self._value = 0

    @property
    def value(self):
        return 1 if self._pin.value else 0

    @value.setter
    def value(self, val: int = 0):
        self._pin.value = bool(val)
