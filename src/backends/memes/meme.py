from flask import Blueprint, request

meme_api = Blueprint("meme_api", __name__)

@meme_api.route("/meme")
def meme():
    pass