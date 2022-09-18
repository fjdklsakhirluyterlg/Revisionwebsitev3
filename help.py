from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from .models import Help

help = Blueprint('helo', __name__)

@help.route("/help/")
def help_view():
    return "no"

@help.route("/help/add", methods=["GET", "POST"])
def add_help():
    if request.method == "POST":
        y = request.form.get("subject")
        x = request.form.get("topic")
        a = request.form.get("question")
        b = request.form.get("awnser")
        c = Help(subject=y, topic=x, question=a, awnser=b)
        db.session.add(c)
        db.session.commit()

@help.route("/help/delete/<id>")
def update_help(id):
    x = db.session.query(Help).filter(Help.id == id).first()
    db.session.delete(x)
    db.session.commit()