from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from .models import Chat, Text, User, Notifications, Reaction
from . import socketio
from flask_socketio import join_room, send, emit
# from . import app

chat = Blueprint("chat", __name__)

@login_required
@chat.route("/chat/add", methods=["GET", "POST"])
def chats_view():
    if request.method == "POST":
        user1 = current_user
        users = request.form["users"].split(" ")
        description = request.form["description"]
        name = request.form["name"]
        new = Chat(description=description, name=name)
        users.append(user1.name)
        for user in users:
            y = User.query.filter_by(name=user).first()
            if y:
                y.chats.append(new)

        db.session.add(new)
        db.session.commit()
        chat_id = getattr(new, "id")
        return redirect(f"/chats/{chat_id}")
        # return jsonify({"id": chat_id})
    else:
        user = request.args.get("user")
        return render_template("chatadd.html", user=user)

@login_required
@chat.route("/chats/<int:id>")
def chat_with_other_users(id):
    chat = Chat.query.filter_by(id=id).first()
    description = chat.description
    id = chat.id
    name = chat.name
    people = []
    ids = []
    Users = db.session.query(User).all()
    for user in Users:
        chats = user.chats
        if chat in chats:
            people.append(user)
            ids.append(user.id)
    
    textsx = []
    texts = db.session.query(Text).all()
    for text in texts:
        if text.chat_id == id:
            textsx.append(text)
    try:
        if current_user.id in ids:
            return render_template("chat.html", people=people, description=description, texts=textsx, id=id, current_user=current_user, name=name)
        else:
            return redirect("/dashboard")
    except:
        return redirect("/login")

@socketio.on("message")
def messageReceived(message):
    room = message["id"]
    text = message["message"]
    name = message["name"]
    data = {"name":name, "message":text}
    # print(f"sendign data: {data}")
    join_room(room)
    socketio.emit("message", data, room=room)
    

@socketio.on("left")
def leftRecieved(message):
    print(f"{message=}")
    socketio.emit(jsonify(message), broadcast=True)


@socketio.on("join")
def joinRoom(message):
    room = message["id"]
    join_room(room)
    data = {"message":"someone joined","name":"admin"}
    socketio.emit("joined", data, room=message["id"])
    
@login_required
@chat.route('/chat/add-text/<id>', methods=["POST"])
def add_text(id):
    if request.method == "POST":
        chat = db.session.query(Chat).filter(Chat.id == id).first()
        text = request.form.get("text")
        authorname = current_user.name
        new_text = Text(text=text, authorname=authorname, chat_id=id)
        db.session.add(new_text)
        db.session.commit()
        c_id = getattr(new_text, "id")
        users = chat.users
        for i in users:
            text = f"<p>{authorname} sent a message in <a href='/chats/{id}'>{chat.name}</a>"
            x = Notifications(text=text, user_id=i.id)
            db.session.add(x)
            db.session.commit()
        return redirect(f"/chats/{id}")

@chat.route("/api/chats/add/text/<id>", methods=["POST"])
def add_text_to_hcat_api(id):
    data = request.get_json()
    chat = db.session.query(Chat).filter(Chat.id == id).first()
    text = data["message"]
    authorname = data["name"]
    new_text = Text(text=text, authorname=authorname, chat_id=id)
    db.session.add(new_text)
    db.session.commit()
    c_id = getattr(new_text, "id")
    users = chat.users
    for i in users:
        text = f"<p>{authorname} sent a message in <a href='/chats/{id}'>{chat.name}</a>"
        x = Notifications(text=text, user_id=i.id)
        db.session.add(x)
        db.session.commit()
    return redirect(f"/chats/{id}")

        
@login_required
@chat.route("/chat/add-reaction/<id>", methods=["POST"])
def add_reaction(id):
    text = db.session.query(Text).filter(Text.id == id).first()
    reaction = request.form.get("reaction")
    authorname = current_user.name
    new_react = Reaction(icon=reaction, author=authorname, text_id=text.id)
    db.session.add(new_react)
    db.session.commit()
    return redirect(f"/chats/{text.chat_id}")

@login_required
@chat.route("/chat/adduser/<id>", methods=["POST", "GET"])
def add_user_to_chat(id):
    if request.method == "POST":
        chat = db.session.query(Chat).filter(Chat.id == id).first()
        user = request.form["user"].split(" ")
        for i in user:
            userx = db.session.query(User).filter(User.name == i).first()
            if userx not in chat.users:
                userx.chats.append(chat)
        
        db.session.commit()
        return redirect(f"/chats/{id}")
    else:
        return render_template("addchatuser.html", id=id)
    
@chat.route("/api/chats")
def chat_api():
    id = request.args.get("id", default=1)
    chat = Chat.query.filter_by(id=id).first()
    dict = {}
    description = chat.description
    id = chat.id
    name = chat.name
    dict["id"] = id
    dict["name"] = name
    dict["description"] = description
    people = []
    ids = []
    Users = db.session.query(User).all()
    for user in Users:
        chats = user.chats
        if chat in chats:
            people.append(user)
            ids.append(user.id)
    
    peoplen = [person.name for person in people]
    dict["peopleids"] = ids
    dict["people"] = peoplen
    
    textsx = []
    texts = db.session.query(Text).all()
    for text in texts:
        if text.chat_id == id:
            textsx.append(text)
    
    h = []
    for i in textsx:
        h.append({"id": i.id, "author" : i.authorname, "time" : i.timestamp, "text": i.text,"reactions" : [reaction.icon for reaction in i.reactions]})
    
    dict["texts"] = h
    
    response = jsonify(dict)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@chat.route('/api/chat/texts')
def get_teh_texts_from_a_chat():
    id = request.args.get("id", default=1)
    chat = Chat.query.filter_by(id=id).first()
    textsx = chat.texts
    h = []
    for i in textsx:
        h.append({"id": i.id, "author" : i.authorname, "time" : i.timestamp, "text": i.text,"reactions" : [reaction.icon for reaction in i.reactions]})
    res = jsonify(h)
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res

@chat.route("/chat/better/work")
def pls_better_chat():
    return render_template("socketchat.html")

@chat.route("/chat/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

# app.register_blueprint(chat, url_prefix="/")