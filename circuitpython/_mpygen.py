#!/usr/bin/env python3

import sys
import shutil
import time
from pathlib import Path
import subprocess as sp
import colorama

colorama.init()

SOURCE = Path('../pybox')
DEST = Path('../mpy')


def check_done(result: bool):
    if result:
        return f"[{colorama.Fore.GREEN} CREATED {colorama.Fore.RESET}]"
    else:
        return f"[{colorama.Fore.RED} SKIPPED {colorama.Fore.RESET}]"


if __name__ == '__main__':
    if not SOURCE.exists():
        print("source destination not found!")
        sys.exit(1)

    # delete dest if exists
    if DEST.exists():
        shutil.rmtree(DEST)

    # create destination
    Path.mkdir(DEST)
    destination = DEST / Path('pybox')
    Path.mkdir(destination)

    start = time.time()

    # iterate over source files and generate mpy files into destination
    for n, src_file in enumerate(SOURCE.glob('*.py'), 1):
        new_file = src_file.stem
        d = destination / Path(f'{new_file}.mpy')
        try:
            sp.run(['./mpy-cross.static-amd64-linux-8.0.3',
                   str(src_file), '-o', d], check=True)
            print(f"{check_done(1)} {d}")
        except:
            print(f"{check_done(0)} {d}")

    print()
    print("===================================================")
    print(f"Done {n} files in {time.time() - start} secs")
    print("===================================================")
