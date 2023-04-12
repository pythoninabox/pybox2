"""
*This module help you to manage the pybox rgb led ring.*

---

Examples:
    >>> from pybox.ring import RING
    >>> from pybox.color import *
    >>> ring = RING()
    >>> ring.write(1)   # turn on whole ring (in RED)
    >>> ring.write(0)   # turn off it
    
The user basically creates an instance of `RING` class. 
This object will creates a data structure (`list`) of PIXEL objects.
`ARING` class is a base class useful for `RING` and `PIXEL`. 
The user never creates an `ARING` object directly. 
A `RING` object is in substance a list of `PIXEL` objects, where a `PIXEL` object
is a representation of a rgb led in the ring.
"""

from neopixel import NeoPixel
import board
from pybox.color import RED, OFF


class ARING:
    NUMBER = 12

    def __init__(self, ctrl_pin=board.GP27, color: tuple[int] = RED, brightness: float = 0.25):
        self._np = NeoPixel(
            ctrl_pin,
            ARING.NUMBER,
            brightness=brightness,
            auto_write=True)

        self._col = [color] * ARING.NUMBER
        self._global_col = color

    def __set_single_led(self, index, color):
        self._np[index] = self.__parse_color(index, color)

    def write(self, col: tuple = None) -> None:
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

    def on(self) -> None:
        self.write(1)

    def off(self) -> None:
        self.write(0)

    def toggle(self) -> None:
        if self._np[0] == OFF:
            self.write(1)
        else:
            self.write(0)

    @property
    def color(self) -> tuple[int]:
        return self._global_col

    @color.setter
    def color(self, col: tuple[int] = RED) -> None:
        self._global_col = col

    @property
    def brightness(self) -> float:
        return self._np.brightness

    @brightness.setter
    def brightness(self, value: float = None) -> None:
        self._np.brightness = value

    def __setitem__(self, index: int, item: tuple[int]) -> None:
        self._np[index] = self.__parse_color(index, item)

    def __getitem__(self, index: int) -> tuple[int]:
        return self._np[index]

    def set_pixel_color(self, index: int = None, col: tuple = None) -> None:
        self._col[index] = col

        if isinstance(index, int):
            self._col[index] = col
        else:
            try:
                if isinstance(index, range):
                    index = list(index)
                for i in index:
                    self._col[i] = col
            except TypeError as exc:
                raise TypeError(
                    "Please, provide an int, a tuple, a list or a range as first arg") from exc

    def get_pixel_color(self, index: int = None) -> tuple[int]:
        return self._col[index]

    def is_on(self, index: int = None) -> bool:
        return self._np[index] != OFF

    def set_pixel(self, index: int = None, col: tuple[int] = None):
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
                    "Please, provide an int, a tuple, a list or a range as first arg") from exc

    def __parse_color(self, index, col=None) -> tuple[int]:
        if col is not None:
            if isinstance(col, tuple):
                if col != OFF:
                    self._col[index] = col
                return col
            elif col == 0:
                return OFF

        return self._col[index]

    def deinit(self):
        self._np.deinit()


class PIXEL:
    """Pixel class.

        A PIXEL object is an abstraction to manage a single rgb led, part of a RING object. 

        Args:
            index (int): index of the pixel in the ring class list. Defaults to None.
            color (tuple[int], optional): color of the Pixel. Defaults to RED.
            ring (ARING, optional): Ring reference. Defaults to None.

        You don't create a PIXEL instance directly, but when you create a RING object, it creates a list of PIXEL objects.

        Examples:
            >>> ring = RING()
            >>> type(ring[0])
            <class 'PIXEL'>
    """

    def __init__(self, index: int = None, color: tuple[int] = RED, ring: ARING = None):
        self.index = index
        self.__ring = ring
        self.__ring.set_pixel_color(index, color)

    def __repr__(self) -> str:
        return f"PIXEL object with index {self.index} and color {self.__ring.get_pixel_color(self.index)}"

    def on(self):
        """Turn on a pixel.

        Examples:
            >>> ring[0].on()   # turn on the pixel at index 0 with current color
        """
        self.__ring.set_pixel(self.index, 1)

    def off(self):
        """Turn off a pixel.

        Examples:
            >>> ring[0].off()   # turn off the pixel at index 0 with current color
        """
        self.__ring.set_pixel(self.index, 0)

    def toggle(self):
        """Turn on a pixel if the pixel is currently turned off and viceversa.
        """
        if self.__ring.is_on(self.index):
            self.off()
        else:
            self.on()

    def write(self, col: tuple = None) -> None:
        """Write a value on a pixel.

        Args:
            col (tuple | int): if a `tuple` set `color` property and use it to turn on it, if a non-zero `int` turn on the pixel using `color`. If zero, turn off it with `pybox.color.OFF`

        Examples:
            >>> ring.write(1)   # turn on all the ring with current global color
            >>> ring.write(0)   # turn off all the ring
        """
        self.__ring.set_pixel(self.index, col)

    @property
    def color(self) -> tuple[int]:
        """Get/Set color of a pixel.

        Returns:
            color: color of the pixel in `tuple[int]` format
        """
        return self.__ring.get_pixel_color(self.index)

    @color.setter
    def color(self, color: tuple[int]):
        self.__ring.set_pixel_color(self.index, color)


class RING:
    """Ring class.

    ---

    Manage the ring of 12 rgb leds on board of pybox

    Args:
        color: color in (r, g, b) format, tipically a pybox.color identifier [ *Default*: pybox.color.RED ].
        brightness: value between 0.0 and 1.0 [ *Default*: 0.25 ].

    Examples:
        >>> ring = RING(color=GREEN)
        >>> ring.write(1)
    """

    def __init__(self, color: tuple[int] = RED, brightness: float = 0.25):
        self.__ring = ARING(color=color, brightness=brightness)
        self.strip = [PIXEL(x, ring=self.__ring) for x in range(12)]

    def __repr__(self) -> str:
        return f"RING object with color {self.__ring._global_col}"

    def __getitem__(self, index: int) -> PIXEL:
        """Get PIXEL object at index.

        Args:
            index: Pixel index

        Returns:
            A Pixel object

        Examples:
            >>> ring[0]             # get first Pixel
        """
        return self.strip[index]

    def on(self):
        """Turn on the ring.

        Examples:
            >>> ring.on()   # turn on all the ring with current global color
        """
        self.__ring.on()

    def off(self):
        """Turn off the ring.

        Examples:
            >>> ring.off()   # turn off all the ring with current global color
        """
        self.__ring.off()

    def toggle(self):
        """Turn on the ring globally if the first Pixel is currently turned off and viceversa.
        """
        self.__ring.toggle()

    def write(self, col: tuple = None) -> None:
        """Manage all the ring globally.

        Args:
            col (tuple | int): if a `tuple` set `full_color` property and use it to turn on/off the whole Ring, if a non-zero `int` turn on the whole Ring using `full_property`. If zero, turn off it with `pybox.color.OFF`

        Examples:
            >>> ring.write(1)   # turn on the ring with current ring color
            >>> ring.write(0)   # turn off the ring
        """
        self.__ring.write(col)

    def deinit(self) -> None:
        """Blank out the ring and release the pin for other use. 
        """
        self.__ring.deinit()

    @property
    def color(self) -> tuple[int]:
        """Get/Set color of the ring.

        Returns:
            color: color of the ring in `tuple[int]` format
        """
        return self.__ring.color

    @color.setter
    def color(self, color: tuple[int]):
        self.__ring.color = color

    @property
    def brightness(self) -> float:
        """Get/Set color of the ring.

        Returns:
            brightness: brightness of the ring in `float` format
        """
        return self.__ring.brightness

    @brightness.setter
    def brightness(self, value: float):
        self.__ring.brightness = value
