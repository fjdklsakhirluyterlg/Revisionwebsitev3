from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from .models import Item, Object, Checkout

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

@shop.route("/api/shop/items")
def view_all_items():
    items = Item.query.all()
    listx = []
    for item in items:
        listx.append({"id":item.id, "title":item.title, "price":item.price, "description":item.description, "stock":item.stock})
    
    return jsonify(listx)

@shop.route("/api/shop/account/create")
def create_shop_acconut():
    pass


@shop.route("/api/shop/checkout/add", methods=["POST"])
def buy_item_thing():
    data = request.get_json()
    user_id = data["user_id"]
    new = Checkout(user_id=user_id)
    db.session.add(new)
    db.session.commit()
    checkout_id = getattr(new, "id")
    for object in data["objects"]:
        obj = Object.query.filter_by(id=int(object)).first()
        itemx = obj.item_id
        print(itemx)
        # item = Item.query.filter_by(id=itemx).first()
        # item.stock -= 1
        obj.checkout_id = checkout_id
    db.session.commit()
    out = getattr(new, "id")
    return jsonify({"id": out})

@shop.route("/api/checkout/buy")
def bu_the_checkout():
    id = request.args.get("id")
    total_price = 0
    checkout = Checkout.query.filter_by(id=id).first()
    userd_id = checkout.user_id
    for object in checkout.objects:
        total_price += object.price
        object.sold = True
        object.user_id = userd_id

    return f"You apyed for {total_price}"

@shop.route("/api/object/view/<id>")
def view_object(id):
    pass

@shop.route("/api/shop/delete/item")
def delete_item_from_shop():
    id = request.args.get("id")
    item = Item.query.filter_by(id=id).first()
    objects = Object.query.filter_by(item_id=item.id).all()
    for obj in objects:
        db.session.delete(obj)
    db.session.delete(item)
    db.session.commit()
    
