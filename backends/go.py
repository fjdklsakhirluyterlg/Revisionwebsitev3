from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
import ctypes
import os

go = Blueprint("go", __name__)

dir = os.getcwd()

if "backends" not in dir:
    dir += "/backends"

library = ctypes.cdll.LoadLibrary(f'{dir}/go_stuff/test.so')

@go.route("/go/test/hello")
def go_test_hello():
    helloq = str(request.args.get("hello"))
    hello = library.hello
    hello.argtypes = [ctypes.c_char_p]
    x = hello(helloq.encode('utf-8'))
    return x