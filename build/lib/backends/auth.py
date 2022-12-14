from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort, escape
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin
from .models import User
from . import db
from flask_mail import Mail, Message
import random
from . import mail
from sqlalchemy import or_
from backends.supplementary.Ahocorasick import AhoCorasick
import random
# from . import app

auth = Blueprint('auth', __name__)

def mank_random_long_id(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    result = ""
    charactersLength = len(characters) - 1
    for i in range(length):
        result += characters[random.randint(0, charactersLength)]
    return result

def validate_user_with_email(address, securitykey, name):
    msg = Message("""verify your email""", sender = 'drive1.banerjee.armaan@outlook.com', recipients=[address])
    msg.html = f"""
    <html>
        <body>
            <h1> Hi {name}</h1>
            <p>Thank you for creating an acount on my website.</p>
            <p>Please validate your email <a href='http://localhost:5090/user/validate/{securitykey}'>here</a>
        </body>
    </html>
    """
    mail.send(msg)
    return {"msg": "sent"}

def make_security_key():
    found = False
    users = User.query.all()
    security_keys = [user.security_key for user in users]
    out = ""
    while not found:
        id = mank_random_long_id(64)
        if id not in security_keys:
            out += id
            found = True

    return out

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        # telephone = request.form["telephone"]
        password = request.form["password"]
        password2 = request.form["password2"]
        # user = User.query.filter_by(email=email).first()
        # if user:
        #     return render_template("signup.html", msg="user already exists")
        # emaile = User.query.filter_by(email=email).first()
        # if emaile:
        #     return render_template("signup.html", msg="user already exists")
        if password != password2:
            return render_template("signup.html", msg="pasword does not match")
        security_key = make_security_key()
        news = User(name=name, email=email, password=generate_password_hash(password, method='sha256'), security_key=security_key)
        db.session.add(news)
        db.session.commit()
        login_user(news, remember=True)
        try:
            validate_user_with_email(address=email, securitykey=security_key, name=name)
        except:
            pass
        return redirect('/dashboard')
    else:
        return render_template("signup.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        name = request.form["name"]
        password = request.form["password"]
        usern = db.session.query(User).filter(or_(User.name == name, User.email == name)).first()
        eid = usern.id
        if not usern:
            return redirect("/signup")
        elif check_password_hash(usern.password, password):
            login_user(usern, remember=True)
            return redirect(f"/dashboard")
        else:
            return render_template("login.html", msg="password is incorrect")
    else:
        return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/login")

@auth.route("/api/auth/user/exists", methods=["POST"])
def does_user_exist_api():
    data = request.get_json()
    name = data["name"]
    escape(name)
    user = User.query.filter_by(name=name).first()
    if user:
        return jsonify({"message":f"{name} already exists"})
    else:
        return jsonify({"message":"user available"})

@auth.route("/api/auth/user/name/reccomend", methods=["POST"])
def reccomend_user_names():
    data = request.get_json()
    name = data["name"]
    if len(name) <= 0:
        return "bad"
    thing = random.randint(0, 1)
    if thing == 0:
        number = random.randint(10, 99)
    else:
        number = random.randint(1970, 2022)

    
# app.register_blueprint(auth, url_prefix="/")