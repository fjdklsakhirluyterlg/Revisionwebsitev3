from ctypes import *
import os

dir = os.getcwd()

loc = f"{dir}/c/square.so"

functions = CDLL(loc)

print(functions.square(10))