from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort, escape
from .import db
from .models import Note
from flask_login import current_user, login_required
from . import socketio
from flask_socketio import join_room


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
    escape(id)
    data = request.get_json()
    text = data["text"]
    note = Note.query.filter_by(id=id).first()
    note.text = text
    db.session.commit()
    return {"id": id}

@notes.route("/notes/delete/<id>")
def delete_note(id):
    escape(id)
    note = Note.query.filter_by(id=id).first()
    db.session.delete(note)
    db.session.commit()
    return jsonify(msg="Deleted")

@login_required
@notes.route("/notes/add")
def add_notes_view():
    return render_template("notes.html")


@login_required
@notes.route("/notes/view/<id>")
def view_note_thing(id):
    escape(id)
    note = Note.query.filter_by(id=id).first()
    if note.user_id == current_user.id:
        return render_template("notes.html", data = note.text, id=note.id)


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
    escape(id)
    note = Note.query.filter_by(id=id).first()
    dict = {}
    dict["id"] = note.id
    dict["text"] = note.text
    dict["user_id"] = note.user_id

    return dict

@socketio.on("note-add")
def user_on_notes(message):
    room = message["id"]

    socketio.emit("note-add", room=room)

@socketio.on("note-change")
def note_change(message):
    room = message["id"]
    join_room(room)
    socketio.emit("note-change", message, room=room)