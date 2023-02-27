import board
import simpleio
import random
import time
from neopixel import NeoPixel
    
pin = board.GP8
led = NeoPixel(board.GP27, 12, brightness=0.25, auto_write=True)


def mtof(m):
    return int(2**((m-69)/12) * 440)

def offset(mseq, o):
    return [ x + o for x in mseq ]

sequence = [
    [18, 67, 788] ,
    [172, 67, 788] ,
    [172, 67, 788] ,
    [170, 63, 548] ,
    [164, 70, 94] ,
    [154, 67, 792] ,
    [170, 63, 550] ,
    [168, 70, 92] ,
    [140, 67, 1752] ,
    [178, 74, 788] ,
    [172, 74, 788] ,
    [170, 74, 788] ,
    [168, 75, 550] ,
    [176, 70, 92] ,
    [144, 66, 790] ,
    [174, 63, 552] ,
    [168, 70, 92] ,
    [140, 67, 1748] ,
    [168, 79, 790] ,
    [176, 67, 550] ,
    [172, 67, 92] ,
    [138, 79, 836] ,
    [122, 78, 550] ,
    [180, 77, 92] ,
    [148, 76, 92] ,
    [148, 75, 68] ,
    [170, 76, 140] ,
    [826, 68, 118] ,
    [362, 73, 836] ,
    [122, 72, 548] ,
    [168, 71, 92] ,
    [148, 70, 92] ,
    [152, 69, 68] ,
    [172, 70, 142] ,
    [822, 63, 116] ,
    [356, 66, 838] ,
    [130, 63, 548] ,
    [160, 67, 92] ,
    [160, 70, 788] ,
    [164, 67, 548] ,
    [180, 70, 94] ,
    [146, 74, 1748] ,
    [166, 79, 788] ,
    [176, 67, 548] ,
    [174, 67, 92] ,
    [132, 79, 840] ,
    [134, 78, 548] ,
    [172, 77, 92] ,
    [150, 76, 92] ,
    [144, 75, 72] ,
    [156, 76, 142] ,
    [826, 68, 118] ,
    [364, 73, 838] ,
    [128, 72, 550] ,
    [154, 71, 92] ,
    [162, 70, 92] ,
    [148, 69, 68] ,
    [174, 70, 142] ,
    [812, 63, 118] ,
    [368, 66, 836] ,
    [118, 63, 548] ,
    [174, 70, 92] ,
    [164, 67, 788] ,
    [164, 63, 592] ,
    [118, 70, 94] ,
    [154, 67, 2000] 
    ]

led.fill((0,0,0))

if __name__ == '__main__':
    for note in sequence:
        led.fill((0,0,0))
        time.sleep(note[0] * 0.0006)
        led.fill((0,0,255))
        simpleio.tone(pin, mtof(note[1] - 12), note[2] * 0.0006)
        
led.fill((0,0,0))    
        