from ctypes import *
import os
from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort

c = Blueprint("c", __name__)

dir = os.getcwd()

if "backends" not in dir:
    dir += "/backends"

loc = f"{dir}/c/square.so"

functions = CDLL(loc)

loc2 = f"{dir}/c/genpi.so"

functions2 = CDLL(loc2)

@c.route("/c/functions/square/<int:num>")
def c_square_num(num):
    x = functions.square(int(num))
    return f"your number squared is {x}"

@c.route("/c/functions/genpi/<int:num>")
def c_gen_pi(num):
    x = functions2.generateπ_from_random(num)
    return f"pi approximation: {x}, for some reason it says 0"