from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from .models import Help
from . import app

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

@help.route("/api/help/add")
def api_add_help():
    try:
        data = request.get_json()
        subject = data["subject"]
        # subject = "test"
        topic = data["topic"]
        # topic = "test"
        question = data["question"]
        # question = "test"
        awnser = data["awnser"]
        # awnser = "test"
        x = Help(subject=subject, topic=topic, question=question, awnser=awnser)
        db.session.add(x)
        db.session.commit()
        return "added!"
    except:
        return jsonify(error="error!")

@help.route("/api/help/view")
def api_view_help():
    subject = request.args.get("subject", default="none")
    if subject != "none":
        y = db.session.query(Help).filter(Help.subject == subject).all()
        return jsonify(message=y)
    else:
        y = db.session.query(Help).all()
    topic = request.args.get("topic", default="none")
    if topic != "none":
        a = db.session.query(Help).filter(Help.topic == topic).all()
    else:
        a = db.session.query(Help.subject).all()
    question = request.args.get("question", default="none")
    if question != "none":
        b = db.session.query(Help.question).filter(Help.question == question).first()
        c = b.awnser
    else:
        b = db.session.query(Help.topic).all()
        c = db.session.query(Help.question).all()
    
    return jsonify(subject=f"y", topic=f"a", question=f"b", awnser=f"c")

app.register_blueprint(help, url_prefix="/")