from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from .import db
from .models import Note
from flask_login import current_user, login_required

notes = Blueprint("notes", __name__)

@notes.route("/api/notes/add", methods=["POST"])
def api_add_a_note_thing():
    data = request.get_json()
    text = data["text"]
    user_id = data["user_id"]

    new = Note(text=text, user_id=user_id)
    db.session.add(new)
    db.session.commit()

    id = getattr(new, "id")
    return {"id": id}

@notes.route("/notes/edit/<id>", methods=["POST"])
def edite_note_thing(id):
    data = request.get_json()
    text = data["text"]
    note = Note.query.filter_by(id=id).first()
    note.text = text
    db.session.commit()
    return {"id": id}

@notes.route("/notes/delete/<id>")
def delete_note(id):
    pass

@login_required
@notes.route("/notes/add")
def add_notes_view():
    return render_template("notes.html")


@login_required
@notes.route("/notes/view/<id>")
def view_note_thing(id):
    note = Note.query.filter_by(id=id).first()
    if note.user_id == current_user.id:
        return render_template("notes.html", data = note.text)


@notes.route("/api/notes/view/all")
def view_all_notes():
    notes = db.session.query(Note).all()
    dict = {}
    for note in notes:
        dict[note.id] = note.text

    # dict = {"hi":"bye"}

    return dict

@notes.route("/api/notes/view/<id>")
def view_single_note(id):
    note = Note.query.filter_by(id=id).first()
    dict = {}
    dict["id"] = note.id
    dict["text"] = note.text
    dict["user_id"] = note.user_id

    return dict


