from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort

from .models import Note

note = Blueprint("note", __name__)

@note.route("/api/notes/add")
def api_add_a_note_thing():
    data = request.get_json()
    text = data["text"]