from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from .models import restauraunt
# from . import app

restauraunts = Blueprint("restauraunts", __name__)

@restauraunts.route("/api/ratings/restaurants/add", methods=["POST"])
def api_add_restuaraunt():
    try: 
        if request.headers['Content-Type'] == 'restaurauntslication/json':
            data = request.get_json()
            name = data["name"]
            overall_rating = float(data["rating"])
            x = restauraunt(name=name, overall_rating=overall_rating)
            db.session.add(x)
            db.session.commit()
            return jsonify(msg="worked")
        else:
            return jsonify(error="wrong stuff")
    except:
        return jsonify(error="error!")

@restauraunts.route("/api/restauraunt/add")
def api_2_restauraunt_add():
    name = request.args.get("name")
    overall_rating = request.args.get("rating")
    x = restauraunt(name=name, overall_rating=overall_rating)
    db.session.add(x)
    db.session.commit()
    return jsonify(message="worked")

@restauraunts.route("/api/restuaraunt/delete")
def api2_restauraunt_delete():
    id = request.args.get("id")
    restaurauntx = db.session.query(restauraunt).filter(restauraunt.id == id).first()
    db.session.delete(restaurauntx)
    db.session.commit()

# app.register_blueprint(restauraunts, url_prefix="/")