from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from .models import boat

boat = Blueprint("boat", __name__)

@boat.route("/api/boat/add")
def api_add_boat():
    name = request.args.get("model", default="test")
    top_speed = request.args.get("topspeed", default=120)
    length = request.args.get("length", default=2.0)
    x = boat(name=name, top_speed=top_speed, length=length)
    db.session.add(x)
    db.session.commit()
    return jsonify(msg="worked")

@boat.route("/api/boat/")
@boat.route("/api/boat/view")
def api_biew_boat():
    x = db.session.query(boat).all()
    dict = {}
    for i in x:
        dict[i.id] = [i.name, i.top_speed, i.length]
    
    return dict

@boat.route("/api/boat/delete")
def api_delete_boat():
    id = request.args.get("id")
    x = db.session.query(boat).filter(boat.id == id).all()
    db.session.delete(x)
    db.session.commit()

@boat.route("/api/boat/search")
def api_boat_search():
    p = request.args.get("p", default="name")
    q = request.args.get("q", default="test")
    if p == "name":
        x = db.session.query(boat).filter(boat.name == q).all()
    elif p == "top-speed":
        x = db.session.query(boat).filter(boat.top_speed == q).all()
    elif p == "length":
        x = db.session.query(boat).filter(boat.length == q).all()
    
    dict = {}
    for i in x:
        dict[i.id] = [i.name, i.top_speed, i.length]
    
    return dict

@boat.route("/api/boat/update/name")
def api_boat_update(request):
    id = request.args.get("id")
    name = request.args.get("name")
    new = request.args.get("new")
    if id:
        boat = db.session.query(boat).filter(boat.id == id).first()
        boat.name = new
        db.session.commit()
        return jsonify(msg="worked")
    
    if name:
        boat = db.session.query(boat).filter(boat.name == name).first()
        boat.name = new
        db.session.commit()
        return jsonify(msg="worked")