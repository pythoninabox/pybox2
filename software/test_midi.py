import board
import synthio
import audiopwmio

data = open("last.mid", "rb")
midi = synthio.from_file(data)
a = audiopwmio.PWMAudioOut(board.GP8)