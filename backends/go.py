from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
import ctypes

library = ctypes.cdll.LoadLibrary('./go_stuff/test.so')
hello_world = library.helloworld
hello_world()

hello = library.hello
hello.argtypes = [ctypes.c_char_p]
hello("everyone".encode('utf-8'))