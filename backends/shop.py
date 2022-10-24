from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from .models import Item

shop = Blueprint("shop", __name__)

@shop.route("/api/shop/item/add")
def add_an_item():
    data = request.get_json()
    description = data["description"]
    title = data["description"]
    price = data["price"]
    stock = data["stock"]