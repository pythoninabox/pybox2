from neopixel import NeoPixel
import board
import time

led = NeoPixel(board.GP14, 8, brightness=0.2, auto_write=True)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 150, 0)
CYAN = (0, 255, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)
MAX = 8
NUMBER = 1
TIME = 0.05

index = 0

for i in range(8):
    led[i] = OFF

while index < 100:
    
    try:
        for i in range(NUMBER):
            led[(i + index) % MAX] = CYAN
        
        time.sleep(TIME)
        
        for i in range(NUMBER):
            led[(i + index) % MAX] = OFF
            
        index += 1
    except KeyboardInterrupt:
        break
      
for i in range(8):
    led[i] = OFF  
    
    
    
    