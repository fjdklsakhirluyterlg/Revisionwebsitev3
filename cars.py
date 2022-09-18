from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from .models import Cars

cars = Blueprint("cars", __name__)

@cars.route("/ratings/cars")
def cars_ratings_show():
    x = db.session.query(Cars.name).all()
    return jsonify(x)

cars.route("/ratings/cars/add", methods=["POST", "GET"])
def cars_ratings_post():
    if request.method == "POST":
        y = request.form.get("name")
        x = Cars(name=y)
        db.session.add(x)
        db.session.commit()

@cars.route("/ratings/cars/delete/<int:id>")
def delete_car(id):
    car = db.session.query(Cars).filter(Cars.id == id).first()
    db.session.delete(car)
    db.session.commit()