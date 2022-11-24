from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
import os
# from . import app

upload = Blueprint("upload", __name__)

UPLOAD_FOLDER = './images/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_required
@upload.route("/upload", methods=["GET", "POST"])
def upload_files_to_server():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        names = []
        for file in request.files.getlist('file'):
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                names.append(filename)
                curdir = os.getcwd()
                namex = f"{current_user.name}.{current_user.id}.{filename}"
                name = os.path.join(f"{curdir}/backends/images/", namex)
                file.save(name)
        
        return "uploaded"
    else:
        return render_template("upload.html")
    
@login_required
@upload.route('/uploads/<filename>')
def see_upload(filename):
    curdir = os.getcwd()
    return send_from_directory(f"{curdir}/backends/images/", filename)

@upload.route("/uploaded/all")
def see_all_files():
    curdir = os.getcwd()
    files = os.listdir(f"{curdir}/backends/images")
    return render_template("files.html", files=files)

@login_required
@upload.route("/uploaded/user/all")
def al_that_user_uploaded():
    curdir = os.getcwd()
    filer = os.listdir(f"{curdir}/backends/images")
    files = []
    for f in filer:
        z = f.split(".")
        if z[1] == str(current_user.id):
            files.append(f)
    return render_template("files.html", files=files)

@login_required
@upload.route("/upload/banner", methods=["GET", "POST"])
def upload_banner_to_server():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        names = []
        for file in request.files.getlist('file'):
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                names.append(filename)
                curdir = os.getcwd()
                namex = f"{current_user.name}.{current_user.id}.{filename}"
                name = os.path.join(f"{curdir}/backends/banners/", namex)
                file.save(name)

        return redirect("/dashboard")
    else:
        return redirect("/dashboard")

@upload.route("/upload/banner/edit")
def edit_banner_photo():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        names = []
        for file in request.files.getlist('file'):
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                names.append(filename)
                curdir = os.getcwd()
                namex = f"{current_user.name}.{current_user.id}.{filename}"
                name = os.path.join(f"{curdir}/backends/banners/", namex)
                file.save(name)

        return redirect("/dashboard")


# app.register_blueprint(upload, url_prefix="/")