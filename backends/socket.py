from . import socketio
from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort

socket = Blueprint("socket", __name__)

@socketio.on("note-change")
def note_change(message):
    pass