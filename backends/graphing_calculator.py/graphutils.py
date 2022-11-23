import numpy as np

def analyse_function(fun):
    fun.lower()
    fun.replace("^", "**")

def sin(x):
    return x - ((x**3)/6) + (x**5)/(120)

def cos(x):
    pass