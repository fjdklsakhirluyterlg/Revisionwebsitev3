from ctypes import *
import os

dir = os.getcwd()

loc = f"{dir}/c/square.c"

functions = CDLL(loc)

print(functions.square(10))