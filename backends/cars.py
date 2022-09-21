from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from .models import Cars
# from . import app

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

@cars.route("/api/cars/add")
def api2_add_cars():
    name = request.args.get("name", default="name")
    brand = request.args.get("brand", default="brange")
    top_speed = request.args.get("top-speed", default=180.0)
    horsepower = request.args.get("horsepower", default=200)
    length = request.args.get("length", default=2.0)
    width = request.args.get("width", default=2.0)
    rating = request.args.get("ratind", default=4.5)
    x = Cars(name=str(name), brand=str(brand), top_speed=float(top_speed), horsepower=int(horsepower), length=float(length), width=float(width), rating=float(rating))
    db.session.add(x)
    db.session.commit()
    return jsonify(msg="worked!")

@cars.route("/api/cars")
def api2_view_cars():
    x = db.session.query(Cars).all()
    dict = {}
    for i in x:
        dict[i.id] = [i.name, i.brand, i.top_speed, i.horsepower, i.length, i.width, i.rating]
    
    return dict

@cars.route("/api/cars/delete")
def api2_cars_delete():
    id = request.args.get("id")
    car = db.session.query(Cars).filter(Cars.id == id).first()
    db.session.delete(car)
    db.session.commit()
    return jsonify(message="worked")

@cars.route("/api/cars/deletecar")
def api2_cars_delete_car():
    name = request.args.get("name")
    car = db.session.query(Cars).filter(Cars.name == name).first()
    db.session.delete(car)
    db.session.commit()
    return redirect(url_for("api2_view_cars"))

@cars.route("/api/cars/search")
def ap2_cars_search():
    p = request.args.get("p", default="name")
    q = request.args.get("q", default="name")
    if p == "name":
        x = db.session.query(Cars).filter(Cars.name == q).all()
    elif p == "brand":
        x = db.session.query(Cars).filter(Cars.brand == q).all()
    elif p == "rating":
        x = db.session.query(Cars).filter(Cars.rating == q).all()
    elif p == "top_speed":
        x = db.session.query(Cars).filter(Cars.top_speed == q).all()
    elif p == "length":
        x = db.session.query(Cars).filter(Cars.length == q).all()
    elif p == "width":
        x = db.session.query(Cars).filter(Cars.width == q).all()
    elif p == "horsepower":
        x = db.session.query(Cars).filter(Cars.horsepower == q).all()
    
    dict = {}
    for i in x:
        dict[i.id] = [i.name, i.brand, i.top_speed, i.horsepower, i.length, i.width, i.rating]
    
    return dict
    
@cars.route("/api/cars/update/name")
def api_cars_update_name(request):
    id = request.args.get("id")
    name = request.args.get("name")
    new_name = request.args.get("new")
    if id:
        car = db.session.query(Cars).filter(Cars.id == id).first()
        car.name = new_name
    if name:
        car = db.session.query(Cars).filter(Cars.name == name).first()
        car.name = new_name
    
    return redirect(url_for("api_view_cars"))

@cars.route("/api/cars/cancel")
def api2_cars_cacnel():
    brand = request.args.get("brand")
    car = db.session.query(Cars).filter(Cars.brand == brand).all()
    for i in car:
        db.session.delete(i)
    db.session.commit()
    return jsonify(msg="worked")

@cars.route("/api/ratings/cars")
def api_cars():
    x = db.session.query(Cars.name).all()
    return jsonify(x)

@cars.route("/api/ratings/cars/add", methods=["POST"])
def api_add_cars():
    try:
        if request.headers['Content-Type'] == 'carslication/json':
            data = request.get_json()
            name = data["name"]
            brand = data["brand"]
            top_speed = data["top-speed"]
            horsepower = data["horsepower"]
            length = data["length"]
            width = data["width"]
            rating = data["rating"]
            x = Cars(name=str(name), brand=str(brand), top_speed=float(top_speed), horsepower=int(horsepower), length=float(length), width=float(width), rating=float(rating))
            db.session.add(x)
            db.session.commit()
            return jsonify(msg="worked!")
        else:
            return jsonify(errors="wrong stuff")
        
    except Exception as errors:
        print(errors)
        return jsonify(errors="there is an error")

# app.register_blueprint(cars, url_prefix="/")