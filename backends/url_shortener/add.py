from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from backends.models import urlshortner
from backends import db
import random

add_url = Blueprint("add_url", __name__)

@add_url.route("/api/urls/shortner/test")
def test_thingy():
    return "here"

def check_if_id_exists(id):
    url = db.session.query(urlshortner).filter_by(id=id).first()
    if url:
        return True
    else:
        return False

def generate_random_id():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    result = ""
    charactersLength = len(characters) - 1
    for i in range(16):
        result += characters[random.randint(0, charactersLength)]
    
    return result


@add_url.route('/api/urls/shortner/add')
def add_url_to_shortenere():
    data = request.get_json()
    free = False
    while not free:
        id = generate_random_id()
