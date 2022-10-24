from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from .models import Item

shop = Blueprint("shop", __name__)

@shop.route("/api/shop/item/add", methods=["POST"])
def add_an_item():
    data = request.get_json()
    description = data["description"]
    title = data["title"]
    price = data["price"]
    stock = int(data["stock"])
    new = Item(description=description, title=title, price=price, stock=stock)
    new.create(stock)
    db.session.add(new)
    db.session.commit()
    id = getattr(new, "id")
    return {"id":id}

@shop.route("/api/items")
def view_all_items():
    items = Item.query.all()
    dictx = {}
    for item in items:
        dictx[item.id] = {"title":item.title, "price":item.price, "description":item.description, "stock":item.stock}
    
