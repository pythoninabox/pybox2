#!/usr/bin/env python

import sys
import subprocess as sp
import mpy_cross as mpy 
from pathlib import Path

input, output = Path('.') / Path(sys.argv[1]), Path('.') / Path(sys.argv[2])

input_files = input.glob("*.py")

for file in input_files:
    #mpy.run(f"-o {output} {file}")
    out = output / Path(f"{file.stem}.mpy")
    mpy.run(f"-o {out} {file}", stdout=sp.PIPE)
    print(out)