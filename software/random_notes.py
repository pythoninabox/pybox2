import time
import rp2pio
import board
import adafruit_pioasm

squarewave = """
.program squarewave
    set pins 1 [31]    ; Drive pin high and then delay for one cycle
    set pins 0 [31]     ; Drive pin low
"""

def mtof(m):
    return int(2**((m-69) / 12) * 440)

seq = (0,2,4,5,7,9,11,12)

assembled = adafruit_pioasm.assemble(squarewave)

sm = rp2pio.StateMachine(
    assembled,
    frequency=1000 * 2,
    first_set_pin=board.GP8,
)                              

"""
sm2 = rp2pio.StateMachine(
    assembled,
    frequency=1000 * 2,
    first_set_pin=board.GP27,
)
"""

sequence = [
    [18, 67, 788] , #onset, #note #duration, example: sm.stop(), time.sleep(18 * 0.0006), note: mtof(67), time.sleep(788 * 0.0006)
    [172, 67, 788] ,
    [172, 67, 788] ,
    [172, 63, 540] ,
    [172, 70, 108] ,
    [140, 67, 792] ,
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
    [154, 67, 1200] 
    ]

bpm = 160
tempo = 30000 / bpm / 1000
final_tempo = tempo / 480

for event in sequence:
    sm.stop()
    time.sleep(event[0] * final_tempo)
    sm.restart()
    sm.frequency = mtof(event[1]) * 32
    time.sleep(event[2] * final_tempo)


sm.stop()
"""
stopped = 1

while True:
    note = input("midi note (36 - 127) > ")
    note = int(note)
    if stopped:
        sm.restart()
        
    sm.frequency = mtof(note) * 32
"""  
