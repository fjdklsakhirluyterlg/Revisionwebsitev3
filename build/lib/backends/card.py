from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from .models import Card, Stack, Quiz, ImageCard
from werkzeug.utils import secure_filename
import os
# from . import app

card = Blueprint("card", __name__)

UPLOAD_FOLDER = './images/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@card.route("/api/stack/add", methods=["POST"])
def api_add_stack():
    data = request.get_json()
    user_id = data["user_id"]
    name = data["name"]
    new = Stack(user_id=user_id, name=name)
    db.session.add(new)
    db.session.commit()
    id = getattr(new, "id")
    for card in data["cards"]:
        front = card["front"]
        back = card["back"]
        new_card = Card(front=front, back=back, stack_id=id)
        db.session.add(new_card)
    db.session.commit()
    
    return jsonify({"id": id})

@card.route("/api/stack/view")
def api_view_stack():
    stacks = Stack.query.order_by(Stack.name)
    dict = {}
    for stack in stacks:
        cards = stack.cards
        correct = 0
        for card in cards:
            if card.correct:
                correct += 1
        
        if len(cards) > 0:
            confidence = correct / len(cards) 
        else:
            confidence = 0
        dict[stack.name] = {"cards" : len(cards), "confidence": confidence}
    
    return dict

@card.route("/api/stack/view/<id>")
def api_view_specific_stack(id):
    stack = Stack.query.filter_by(id=id).first()
    cards = stack.cards
    dict = {}
    dict["cards"] = []
    correct = 0
    for card in cards:
        card_dict = {}
        card_dict["front"] = card.front
        card_dict["back"] = card.back
        card_dict["correct"] = card.correct
        if card.correct:
            correct += 1
        dict["cards"].cardend(card_dict)
    
    dict["name"] = stack.name
    dict["user_id"] = stack.user_id
    dict["confidence"] = correct/len(cards)
    dict["length"] = len(cards)
    
    return dict

@card.route("/api/stack/card/view/<id>")
def api_view_specific_card(id):
    card = Card.query.filter_by(id=id).first()
    dict = {}
    dict["front"] = card.front
    dict["back"] = card.back
    stack = Stack.query.filter_by(id=card.stack_id).first()
    dict["stack name"] = stack.name
    dict["stack id"] = card.stack_id
    dict["id"] = id
    return dict

@card.route("/api/stack/cards/add", methods=["POST"])
def api_card_add_stuff():
    data = request.get_json()
    front = data["front"]
    back = data["back"]
    stack_id = data["id"]
    new = Card(front=front, back=back, stack_id=stack_id)
    db.session.add(new)
    db.session.commit()
    id = getattr(new, "id")
    for file in request.files.getlist('file'):
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            curdir = os.getcwd()
            new_image = ImageCard(card_id=id, filename=filename)
            db.session.add(new_image)
            db.session.commit()
            namex = getattr(new_image, "id")
            name = os.path.join(f"{curdir}/src/backends/cards/", f"{namex}.{filename}")
            file.save(name)
    return jsonify({"id": id})
    
@card.route("/api/stack/cards/delete")
def api_cards_delete_stuff():
    id = request.args.get("id")
    card = Card.query.filter_by(id=id).first()
    db.session.delete(card)
    db.session.commit()

@card.route("/api/stack/cards/correct")
def api_make_card_correct():
    id = request.args.get("id")
    card = Card.query.filter_by(id=id).first()
    card.correct = True
    db.session.commit()

@card.route("/api/stack/cards/false")
def api_make_card_incorrect():
    id = request.args.get("id")
    card = Card.query.filter_by(id=id).first()
    
@card.route("/cards/view/<user>/<name>/<id>")
def veiw_stack_things(user, name, id):
    stack = Stack.query.filter_by(id=id).first()
    return render_template("stack.html", stack=stack)

@card.route("/cards/test/<user>/<name>/<id>")
def test_user_on_cards(id):
    stack = Stack.query.filter_by(id=id).first()

@card.route("/cards/check/front")
def check_front_if_true():
    data = request.get_json()
    card_id = data["card_id"]
    awnser = data["awnser"]
    card = Card.query.filter_by(id=card_id).first()
    if card.front == awnser:
        return jsonify({"msg": "correct"})
    return jsonify({"msg": "incorrect"})

@card.route("/cards/check/back")
def check_back_if_true():
    data = request.get_json()
    card_id = data["card_id"]
    awnser = data["awnser"]
    card = Card.query.filter_by(id=card_id).first()
    if card.back == awnser:
        return jsonify({"msg": "correct"})
    return jsonify({"msg": "incorrect"})

@card.route("/api/stack/delete/<id>")
def delete_stack_from_id(id):
    stack = Stack.query.filter_by(id=id).first()
    for card in stack.cards:
        db.session.delete(card)
    db.session.delete(stack)
    db.session.commit()
    return "deleted"

@card.route("/api/stack/quiz/make/<id>")
def make_a_stack_a_quiz(id):
    stack = Stack.query.filter_by(id=id).first()
    new = Quiz(user_id=stack.user_id, name=stack.name, description="Quiz")
    db.session.add(new)
    db.session.commit()
    quiz_id = getattr(new, "id")
    fronts = []
    backs = []
    for card in stack.cards:
        fronts.append(card.front)
        backs.append(card.back)

@login_required
@card.route("/stack/fork/<id>")
def fork_stack_of_cards(id):
    stack = Stack.query.filter_by(id=id).first()
    new_stack = Stack(name=stack.name, user_id=current_user.id)
    db.session.add(new_stack)
    db.session.commit()
    stack_id = getattr(new_stack, "id")
    for card in stack.cards:
        new_card = Card(front=card.front, back=card.back, stack_id=stack_id)
        db.session.add(new_card)
    db.session.commit()
    return "forked"

@card.route("/cards/edit/<id>")
def edit_a_card_please(id):
    card = Card.query.filter_by(id=id).first()
    data = request.get_json()
    card.front = data["front"]
    card.back = data["back"]
    db.session.commit()

@card.route("/stack/add")
def view_stack_add():
    return render_template("cardadd.html")
    
# app.register_blueprint(card, url_prefix="/")