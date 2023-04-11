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
    """Aring class.

    ---

    Args:
        color: color in (r, g, b) format, tipically a pybox.color identifier [ *Default*: pybox.color.RED ].
        brightness: value between 0.0 and 1.0 [ *Default*: 0.25 ].

    Examples:
        >>> ring = RING(color=GREEN)
        >>> ring.write(1)
    """
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
        """Manage all the ring globally.

        Args:
            col (tuple | int): if a `tuple` set `full_color` property and use it to turn on/off the whole Ring, if a non-zero `int` turn on the whole Ring using `full_property`. If zero, turn off it with `pybox.color.OFF`

        Examples:
            >>> ring.write(1)   # turn on all the ring with current global color
            >>> ring.write(0)   # turn off all the ring
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

    def on(self) -> None:
        """Turn on the ring globally.

        Examples:
            >>> ring.on()   # turn on all the ring with current global color
        """
        self.write(1)

    def off(self) -> None:
        """Turn off the ring globally.

        Examples:
            >>> ring.off()  # turn off the ring
        """
        self.write(0)

    def toggle(self) -> None:
        """Turn on the ring globally if the first Pixel is currently turned off and viceversa.

        """
        if self._np[0] == OFF:
            self.write(1)
        else:
            self.write(0)

    @property
    def color(self) -> tuple[int]:
        """Get or set the global color used in `write` method

        Args:
            col (tuple[int]): color in tuple format, you can use pybox.color identifier. [ *Default*: `pybox.color.RED` ].

        Examples:
            >>> ring.color = CYAN   # set global color to pubox.color.CYAN
            >>> ring.color          # get global color
        """

        return self._global_col

    @color.setter
    def color(self, col: tuple[int] = RED) -> None:
        self._global_col = col

    @property
    def brightness(self) -> float:
        """Get or set brightness (only at global level)

        Args:
            value (float): float between 0.0 (min brightness) and 1.0 (max brightness)
        """
        return self._np.brightness

    @brightness.setter
    def brightness(self, value: float = None) -> None:
        self._np.brightness = value

    def __setitem__(self, index: int, item: tuple[int]) -> None:
        """Set a pixel as list item

        Description: 
            a Ring is basically a list of Pixel. At a lower level you can set a single (or a group of) 
            Pixel(s) using slice notation. Preferably you shoud use `set` method

        Args:
            index: pixel index [ *Required* ]
            item: tuple for RGB desc [ *Default*: `None`]

        Examples:
            >>> ring[0] = GREEN
            >>> ring[1:3] = [GREEN, GREEN]
        """
        self._np[index] = self.__parse_color(index, item)

    def __getitem__(self, index: int) -> tuple[int]:
        """Get color at index.

        Args:
            index: Pixel index

        Examples:
            >>> ring[0] = GREEN     # set first Pixel
            >>> ring[0]             # get first Pixel
            (0, 255, 0)
        """
        return self._np[index]

    def set_pixel_color(self, index: int = None, col: tuple = None) -> None:
        """Set single Pixel color.

        Args:
            index: position index of Pixel
            col: color in (r, g, b) color. Tipically an identifier from `pybox.color` [ *Default*: `None` ].
        """
        self._col[index] = col

        if isinstance(index, int):
            # self.__set_single_led(index, col)
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
        """Get single Pixel color.
        """
        return self._col[index]

    def is_on(self, index: int = None) -> bool:
        """Verify if a Pixel is on

        Args:
            index (int, optional): index of the pixel to check. Defaults to None.

        Returns:
            bool: True if the pixel at index is on, otherwise False
        """
        return self._np[index] != OFF

    def set_pixel(self, index: int = None, col: tuple[int] = None):
        """set color of a (group of) Pixel(s).

        You can set a single Pixel with a int number. Alternatively you can set a group of Pixels with a list (or tuple) 
        or using a range instance.

        Args:
            index (int, list, tuple, range): index of Pixel(s) [ *Required* ]
            col (tuple[int], optional): _description_. [ *Default*: `None` ]

        Examples:
            >>> ring.set_pixel(0, GREEN)            # turn on the Pixel at index 0 (in green)
            >>> ring.set_pixel([0,1,2], BLUE)       # turn on first three Pixels (in blue)
            >>> ring.set_pixel(range(0,12,2), RED)  # turn on all Pixels at even positions (in red)
            >>> ring.set_pixel(0, OFF)              # turn off the Pixel at index 0
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

        You don't create a PIXEL instance directly, but when you create a RING object, it creates a list of PIXEL objects.

        Args:
            index (int): index of the pixel in the ring class list. Defaults to None.
            color (tuple[int], optional): color of the Pixel. Defaults to RED.
            ring (ARING, optional): Ring reference. Defaults to None.

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
