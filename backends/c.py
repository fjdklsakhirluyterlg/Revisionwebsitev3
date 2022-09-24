from ctypes import *
from pathlib import Path

dir = Path(Path.cwd()).parent

loc = f"{dir}/c/square.c"

functions = CDLL(loc)

print(functions.square(10))