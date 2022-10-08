from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from .import db
from .models import Note

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


