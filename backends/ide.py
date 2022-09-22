from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
import subprocess
import random
import os
# from . import app

ide = Blueprint("ide", __name__)

@ide.route("/ide/docs")
def ide_docs():
    return "This is an ide for stuff do not try and break me please"
    

@ide.route("/ide/python", methods=["GET", "POST"])
def python_ide():
    if request.method == "POST":    
        x = request.form.get("script")
        num = random.randint(0, 100000)
        path = f"./programs/file{num}.py"
        with open(path, "w+") as file:
            file.write(x)
        
        command = f'python {path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return render_template("idepy.html", output=output.decode('utf-8'), error=error.decode('utf-8'), code=x)
    
    else:
        return render_template("idepy.html")
    
    # y = exec(open('file.py').read())
    # return "result: {y}"
    # return redirect(url_for("run_python_ide"))

@ide.route("/ide/python/run")
def run_python_ide():
    command = f'python file.py'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return f"result: {output}, error: {error}"

@ide.route("/ide/js", methods=["GET", "POST"])
def nodejs_ide():
    if request.method == "POST":
        x = request.form.get("script")
        with open("file.js", "w") as file:
            file.write(x)
        
        command = f'node file.js'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return render_template("idejs.html", output=output.decode('utf-8'), error=error.decode('utf-8'))
    else:
        return render_template("idejs.html")
    
@ide.route("/ide/ts", methods=["GET", "POST"])
def nodets_ide():
    if request.method == "POST":
        x = request.form.get("script")
        with open("file.ts", "w") as file:
            file.write(x)
        
        command = f'node file.ts'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return render_template("idets.html", output=output.decode('utf-8'), error=error.decode('utf-8'))
    else:
        return render_template("idets.html")

@ide.route("/ide/cpp", methods=["GET", "POST"])
def cpp_ide():
    if request.method == "POST":
        x = request.form.get("script")
        with open("file.cpp", "w") as file:
            file.write(x)
        
        command = f'g++ file.cpp -o file.exe && ./file.exe'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return render_template("idecpp.html", output=output.decode('utf-8'), error=error.decode('utf-8'))
    else:
        return render_template("idecpp.html")

# app.register_blueprint(ide, url_prefix="/")