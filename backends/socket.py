from . import socketio

@socketio.on("note-change")
def note_change(message):
    pass