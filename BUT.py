from pybox.button import SIMPLEBUTTON
from pybox.ring import RING
import time

button = SIMPLEBUTTON()
previous_value = 0
status = 0
ring = RING()


while True:
    current_value = button.value
    
    if current_value == 1 and previous_value == 0:
        status = not status
        print(int(status))
    
    if status == 1:
        ring.on()
    else:
        ring.off()
        
    previous_value = current_value