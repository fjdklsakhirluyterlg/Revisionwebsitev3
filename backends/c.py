from ctypes import *

loc = "../c/square.so"

functions = CDLL(loc)

print(functions.square(10))