import flask_sqlalchemy
from backends import db

def add(thing):
    db.session.add(thing)
    
