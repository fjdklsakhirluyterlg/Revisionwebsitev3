from . import socketio
from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from flask_socketio import join_room

socket = Blueprint("socket", __name__)

@socketio.on("note-changes")
def note_change(message):
    room = message["id"]
    join_room(room)
    socketio.emit("note-changed", message, room=room)