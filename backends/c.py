from ctypes import *
import os

dir = os.getcwd()

loc = f"{dir}/c/square.so"

functions = CDLL(loc)

loc2 = f"{dir}/c/genpi.so"

functions2 = CDLL(loc2)

print(functions.square(10))
print(functions2.generateπ_from_random(1000))