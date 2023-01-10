from flask import Blueprint, request, josnify

meme_api = Blueprint("meme_api", __name__)

@meme_api.route("/meme")
def meme():
    return ""

@meme_api.route("api/meme/add", methods=["POST"])
def add_meme_thing():
    data = request.get_json()