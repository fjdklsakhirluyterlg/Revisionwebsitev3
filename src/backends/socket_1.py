from . import socketio
from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from flask_socketio import join_room

socket = Blueprint("socket", __name__)

@socketio.on("note-changes")
def note_change(message):
    room = message["id"]
    join_room(room)
    socketio.emit("note-changed", message, room=room)

@socketio.on("new-notification")
def new_notification_recieved(message):
    user = message["user_id"]
    join_room(user)
    socketio.emit("new-notification", message, room=user)


def emit_new_notification(text, user_id):
    join_room(user_id)
    socketio.emit("new-notification", text, room=user_id)

def emit_new_thing():
    pass
