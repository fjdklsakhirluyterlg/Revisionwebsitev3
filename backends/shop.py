from pydoc import describe
from xml.sax.handler import feature_external_ges
from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from .models import Item, Object, Checkout, User, Shopaccount
from werkzeug.utils import secure_filename
import os
import markdown

shop = Blueprint("shop", __name__)

UPLOAD_FOLDER = './shop/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@shop.route("/api/shop/item/add", methods=["POST"])
def add_an_item():
    data = request.get_json()
    description = data["description"]
    title = data["title"]
    price = data["price"]
    stock = int(data["stock"])
    new = Item(description=description, title=title, price=price, stock=stock)
    db.session.add(new)
    db.session.commit()
    id = getattr(new, "id")
    for i in range(stock):
        new_object = Object(item_id=id, price=price)
        db.session.add(new_object)
    db.session.commit()
    return {"id":id}

@shop.route("/api/shop/items")
def view_all_items():
    items = Item.query.all()
    listx = []
    for item in items:
        listx.append({"id":item.id, "title":item.title, "price":item.price, "description":item.description, "stock":item.stock})
    
    return jsonify(listx)

@shop.route("/shop/add", methods=["POST", "GET"])
def view_add_for_shopadd():
    if request.method == "POST":
        title = request.form.get("title").replace(" ", "-")
        price = request.form.get("price")
        stock = int(request.form.get("stock"))
        description = markdown.markdown(request.form.get("description"))
        new = Item(description=description, title=title, price=price, stock=stock)
        db.session.add(new)
        db.session.commit()
        id = getattr(new, "id")
        for i in range(stock):
            new_object = Object(item_id=id, price=price)
            db.session.add(new_object)
        db.session.commit()

        curdir = os.getcwd()
        count = 0
        os.mkdir(f"{curdir}/backends/shop/{id}")
        for file in request.files.getlist('file'):
            count += 1
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                namex = f"{count}.{filename}"
                name = os.path.join(f"{curdir}/backends/shop/{id}", namex)
                file.save(name)

        return redirect(f"/shop/view/{title}")
    else:
        return render_template("itemadd.html")

@shop.route("/api/shop/account/create")
def create_shop_acconut():
    data = request.get_json()
    user_id = data["user_id"]
    user = User.query.filter_by(id=user_id).first()
    description = data["description"]
    if not user.description:
        user.description = description
        db.session.commit()
    credit_card = data["credit_card"]
    telephon = ""
    if "telephone" in data:
        telephon += data["telephone"]
    new = Shopaccount(user_id=user_id, credit_card=credit_card, telephone=telephon)

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        item = array[0]
        pivot = item.created_at
        less = [i for i in array[1:] if i.created_at <= pivot]
        greater = [i for i in array[1:] if i.created_at > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

@shop.route("/api/shop/checkout/add", methods=["POST"])
def buy_item_thing():
    data = request.get_json()
    user_id = int(data["user_id"])
    things = []
    check = Checkout.query.filter_by(user_id=user_id).all()
    for itm in check:
        if not itm.sold:
            things.append(itm)
    if len(things) > 0:
        stuff = quick_sort(things)[-1]
        checkout_id = stuff.id
    else:
        new = Checkout(user_id=user_id)
        db.session.add(new)
        db.session.commit()
        checkout_id = getattr(new, "id")
    
    for object in data["objects"]:
        obj = Object.query.filter_by(id=int(object)).first()
        itemx = obj.item_id
        # print(itemx)
        item = Item.query.filter_by(id=itemx).first()
        item.stock -= 1
        obj.checkout_id = checkout_id
    db.session.commit()
    return jsonify({"id": checkout_id})

@shop.route("/api/checkout/buy")
def bu_the_checkout():
    id = request.args.get("id")
    total_price = 0
    checkout = Checkout.query.filter_by(id=id).first()
    userd_id = checkout.user_id
    for object in checkout.objects:
        total_price += int(object.price)
        object.sold = True
        object.user_id = userd_id

    return f"You apyed for {total_price}"

@shop.route("/api/object/view/<id>")
def view_object(id):
    object = Object.query.filter_by(id=id).first()
    dic = {}
    dic["id"] = object.id
    dic["item_id"] = object.item_id
    dic["price"] = object.price
    return dic

@shop.route("/images/<filename>/<id>")
def see_image_thing(filename, id):
    curdir = os.getcwd()
    return send_from_directory(f"{curdir}/backends/shop/{id}/", filename)

@shop.route("/shop/view/<title>")
def view_item(title):
    item = Item.query.filter_by(title=title).first()
    userid = item.user_id
    # user = User.query.filter_by(id=userid).first()
    # name = user.name
    description = item.description
    images = os.listdir(f"./backends/shop/{item.id}")
    images.sort()
    mainimage = images[0]
    id=item.id
    price=item.price
    stock=item.stock
    stuff = []
    objects=item.objects
    for obj in objects:
        if not obj.sold:
            stuff.append(obj.id)
    
    user_id = None
    if current_user.is_authenticated:
        user_id = current_user.id
    return render_template("item.html", files=images, mainimage=mainimage, title=title, description=description, id=id, price=price, stock=stock, items=stuff, user_id=user_id)


@shop.route("/api/shop/delete/item")
def delete_item_from_shop():
    id = request.args.get("id")
    item = Item.query.filter_by(id=id).first()
    objects = Object.query.filter_by(item_id=item.id).all()
    for obj in objects:
        db.session.delete(obj)
    db.session.delete(item)
    db.session.commit()
    
@login_required
@shop.route("/shop/user/basket")
def get_current_basket():
    checkouts = current_user.checkouts
    basket = []
    for check in checkouts:
        if not check.sold:
            basket.append(check)

    actual = basket[0]
    dict = {"objects":[]}
    items = []
    for obj in actual.objects:
        dict["objects"].append(obj.id)
        itemx = obj.item_id
        item = Item.query.filter_by(id=itemx).first()
        items.append(item.title)
    dict["created_at"] = actual.created_at
    dict["items"] = list(set(items))
    if actual.sold:
        dict["sold"] = True
    else:
        dict["sold"] = False
    return dict

@shop.route("/shop/search")
def search_shop():
    query = request.args.get("q")