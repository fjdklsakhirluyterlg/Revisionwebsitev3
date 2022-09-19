from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from .models import airplane
from . import app

airplanes = Blueprint("airplanes", __name__)

@airplanes.route("/api/ratings/airplane/add", methods=["POST"])
def api_add_planes():
    try:
        if request.headers['Content-Type'] == 'airplanelication/json':
            data = request.get_json()
            type = data["type"]
            length = data["length"]
            width = data["width"]
            # altitude = data["altitude"]
            top_speed = data["top-speed"]
            airline = data["airline"]
            base = data["base"]
            x = airplane(type=type, length=length, width=width, top_speed=top_speed, airline=airline, base=base)
            db.session.add(x)
            db.session.commit()
            return jsonify(msg="worked!")
        else:
            return jsonify(error="wrong stuff")
    except:
        return jsonify(error="something went wrong")

@airplanes.route("/api/airplane")
def api2_view_airplane():
    x = db.session.query(airplane).all()
    dict = {}
    for i in x:
        dict[i.id] = [i.type, i.length, i.width, i.top_speed, i.airline, i.base]
    return dict

@airplanes.route("/api/airplane/add")
def api2_add_airplane():
    type = request.args.get("type", default="A320")
    length = request.args.get("length", default=200.0)
    width = request.args.get("width", default=30)
    top_speed = request.args.get("top", default=790)
    airline = request.args.get("airline", default="BA")
    base = request.args.get("base", default="heathrow")
    x = airplane(type=type, length=length, width=width, top_speed=top_speed, airline=airline, base=base)
    db.session.add(x)
    db.session.commit()
    return jsonify(msg="worked!")

@airplanes.route("/api/airplane/delete")
def api2_airplane_delete():
    id = request.args.get("id")
    airplanex = db.session.query(airplane).filter(airplane.id == id).first()
    db.session.delete(airplanex)
    db.session.commit()
    return redirect(url_for("api2_view_airplane"))

@airplanes.route("/api/airplane/update/name")
def api2_airplane_update_name():
    id = request.args.get("id")
    new_name = request.args.get("name")
    plane = db.session.query(airplane).filter(airplane.id == id).first()
    plane.name = new_name
    db.session.commit()
    return jsonify(msg="worked")

@airplanes.route('/api/airplane/update/airline')
def update_airline_api_airplane():
    id = request.args.get("id")
    new_airplne = request.args.get("airline")
    plane = db.session.query(airplane).filter(airplane.id == id).first()
    plane.airline = new_airplne
    db.session.commit()
    return jsonify(msg="updated")

@airplanes.route('/api/airplane/update/base')
def update_base_api_airplane():
    id = request.args.get("id")
    new_base = request.args.get("base")
    plane = db.session.query(airplane).filter(airplane.id == id).first()
    plane.base = new_base
    db.session.commit()
    return jsonify(msg="worked")

@airplanes.route("/api/airplane/search")
def api2_airplane_search():
    p = request.args.get("p", default="type")
    q = request.args.get("q", default="A320")
    if p == "type":
        x = db.session.query(airplane).filter(airplane.type == q).all()
    elif p == "airline":
        x = db.session.query(airplane).filter(airplane.airline == q).all()
    elif p == "length":
        x = db.session.query(airplane).filter(airplane.length == q).all()
    elif p == "width":
        x = db.session.query(airplane).filter(airplane.width == q).all()
    elif p == "base":
        x = db.session.query(airplane).filter(airplane.base == q).all()
    elif p == "top":
        x = db.session.query(airplane).filter(airplane.top_speed == q).all()
    
    dict = {}
    for i in x:
        dict[i.id] = [i.type, i.length, i.width, i.top_speed, i.airline, i.base]
    return dict