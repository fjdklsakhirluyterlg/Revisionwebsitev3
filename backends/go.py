import ctypes

library = ctypes.cdll.LoadLibrary('./go_stuff/test.so')
hello_world = library.helloworld
hello_world()