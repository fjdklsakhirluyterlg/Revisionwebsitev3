from flask import Flask, request, Blueprint

socail_media = Blueprint("social_media", __name__)

@socail_media.route("/api/social/test")
def test_res():
    return "spend less time on it"