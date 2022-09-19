from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from .models import bank_user

bank = Blueprint("bank", __name__)

@bank.route("/api/bank/add")
def api_bank_add():
    name = request.args.get("name", default="test")
    money = request.args.get("money", default=20.0)
    type = request.args.get("type", default="standard")
    x = bank_user(name=name, money=money, account_type=type)
    db.session.add(x)
    db.session.commit()
    return redirect(url_for("api_bank_view"))

@bank.route("/api/bank")
@bank.route("/api/bank/view")
def api_bank_view():
    x = db.session.query(bank_user).all()
    dict = {}
    for i in x:
        dict[i.id] = [i.name, i.money, i.account_type]
    return dict

@bank.route("/api/bank/delete")
def api_delete_bank():
    id = request.args.get("id")
    x = db.session.query(bank_user).filter(bank_user.id == id).first()
    db.session.delete(x)
    db.session.commit()
    return redirect(url_for("api_bank_view"))

@bank.route("/api/bank/deleteuser")
def api_delete_user():
    name = request.args.get("name")
    x = db.session.query(bank_user).filter(bank_user.name == name).first()
    db.session.delete(x)
    db.session.commit()
    return redirect(url_for("api_bank_view"))

@bank.route("/api/bank/search")
def api_bank_search():
    p = request.args.get("p", default="name")
    q = request.args.get("q", default="test")
    if p == "account_type":
        x = db.session.query(bank_user).filter(bank_user.account_type == q).all()
    elif p == "name":
        x = db.session.query(bank_user).filter(bank_user.name == q).all()
    dict = {}
    for i in x:
        dict[i.id] = i.name

@bank.route("/api/bank/update/name")
def api_update_name_bank(request):
    id = request.args.get("id")
    new_name = request.args.get("name")
    user = db.session.query(bank_user).filter(bank_user.id == id).first()
    user.name = new_name
    db.session.commit()
    return jsonify(message="worked")