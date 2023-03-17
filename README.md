# python in a box (pybox)

## circuitpython installation

1. Mount pybox via usb
2. Copy circuipython uf2 file inside `/circuitpython` folder
3. Copy all content inside `/lib` into `/CIRCUITPY/lib`, alternatively use `install.sh` script (only for linux)

## Upgrade pybox package

Copy `src/pybox` into `CIRCUITPY/lib`

## Simple Usage

There are six modules in this package:
1. **led**, to manage a single led (internalor external, as a part of ring led strip)
2. **button**, to manage the button
3. **pot**, to manage the potentiometer
4. **ring**, to manage the led ring
5. **tone**, to manage tone production, and send them to the internal speaker

### led module

#### example:

```py
from pybox.led import LED

# choose external led
led = LED('external') 

# led on
led.on()

#led off
led.off()
```

#### api

```py
# constructor
led = pybox.led.LED(target='internal')

# on and off 
led.on()
led.off()

# toggle: off if led is on and viceversa
led.toggle()

# write a digital value on led (0 or 1) an color it
led.write(1, GREEN)
led.write(0)
```