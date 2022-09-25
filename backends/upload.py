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
                name = os.path.join(f"{curdir}/backends/images/", filename)
                file.save(name)
        
        return "uploaded"
    else:
        return render_template("upload.html")
    
@login_required
@upload.route('/uploads/<filename>')
def see_upload(filename):
    curdir = os.getcwd()
    return send_from_directory(f"{curdir}/backends/images/", filename)

@login_required
@upload.route("/uploaded/all")
def see_all_files():
    curdir = os.getcwd()
    files = os.listdir(f"{curdir}/backends/images")
    


# app.register_blueprint(upload, url_prefix="/")