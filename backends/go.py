import ctypes

library = ctypes.cdll.LoadLibrary('./go_stuff/test.so')
hello_world = library.helloworld
hello_world()

hello = library.hello
hello.argtypes = [ctypes.c_char_p]
hello("everyone".encode('utf-8'))