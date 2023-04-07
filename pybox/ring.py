"""
*This module help you to manage the pybox rgb led ring.*

---

Examples:
    >>> from pybox.ring import RING
    >>> from pybox.color import *
    >>> ring = RING()
    >>> ring.fill(1)    # turn on whole ring (in RED)
    >>> ring.fill(0)    # turn off it
    
The user basically should use only the `RING` class inside it. Every led in the Ring is called Pixel and substantially a Ring is a list of Pixels.  
"""

from neopixel import NeoPixel
import board
from pybox.color import RED, OFF


class RING:
    """Ring class.

    Args:
        color: color in (r, g, b) format, tipically a pybox.color identifier [*default*: pybox.color.RED].
        brightness: value between 0.0 and 1.0 [*default*: 0.25].

    Examples:
        >>> ring = RING(color=GREEN)
        >>> ring.fill()
    """
    NUMBER = 12

    def __init__(self, ctrl_pin=board.GP27, color: tuple[int] = RED, brightness: float = 0.25):
        self._np = NeoPixel(
            ctrl_pin,
            RING.NUMBER,
            brightness=brightness,
            auto_write=True)

        self._col = [color] * RING.NUMBER
        self._global_col = color

    def __setitem__(self, index: int, item: tuple[int]):
        """set a pixel as list item

        Description: 
            a Ring is basically a list of Pixel. At a lower level you can set a single (or a group of) 
            Pixel(s) using slice notation. Preferably you shoud use `set` method

        Args:
            index: pixel index
            item: tuple for RGB desc

        Examples:
            >>> ring[0] = GREEN
            >>> ring[1:3] = [GREEN, GREEN]
        """
        self._np[index] = self.__parse_color(index, item)

    def __getitem__(self, index: int):
        """get color at index.

        Args:
            index: Pixel index

        Examples:
            >>> ring[0] = GREEN
            >>> ring[0]
            (0, 255, 0)
        """
        return self._np[index]

    def set(self, index: int = None, col: tuple[int] = None):
        """set color of a (group of) Pixel(s).

        You can set a single Pixel with a int number. Alternatively you can set a group of Pixels with a list (or tuple) 
        or using a range instance.

        Args:
            index (int, list, tuple, range): index of Pixel(s). Defaults to None.
            col (tuple[int], optional): _description_. Defaults to None.

        Examples:
            >>> ring.set(0, GREEN)              # turn on in green Pixel at index 0
            >>> ring.set([0,1,2], BLUE)         # turn on in blue first three Pixels
            >>> ring.set(range(0,12,2), RED)    # turn on in red all Pixels at even positions
        """
        if isinstance(index, int):
            self.__set_single_led(index, col)
            return None
        else:
            try:
                if isinstance(index, range):
                    index = list(index)
                for i in index:
                    self.__set_single_led(i, col)
                return None
            except TypeError as exc:
                raise TypeError(
                    "Please, provide an int, a tuple or a list as first arg") from exc

    def __set_single_led(self, index, color):
        self._np[index] = self.__parse_color(index, color)

    def fill(self, col: tuple = None):
        """manage all the ring globally.


        Args:
            col (tuple or int): this arg can be: 

                - `tuple`: set `self.full_color` property and use it to turn on/off the whole Ring
                - `int`: if non zero, turn on the whole Ring using `self.full_property`. If zero, turn off it with pybox.color.OFF
        """
        if col is not None:
            if isinstance(col, tuple):
                if col != OFF:
                    self._global_col = col
                _col = col
            elif col == 0:
                _col = OFF
            else:
                _col = self._global_col
        else:
            _col = self._global_col

        self._np.fill(_col)

    @property
    def full_color(self, col: tuple[int] = RED):
        """get or set the global color used in `fill` method

        Args:
            col (tuple[int]): color in tuple format, you can use pybox.color identifier. [ *Default*: pybox.color.RED ].
        """

        self._global_col = col

    @full_color.setter
    def full_color(self):
        return self._global_col

    def set_color(self, index, col=None):
        self._col[index] = col

    def __parse_color(self, index, col=None):
        if col is not None:
            if isinstance(col, tuple):
                if col != OFF:
                    self._col[index] = col
                return col
            elif col == 0:
                return OFF

        return self._col[index]
