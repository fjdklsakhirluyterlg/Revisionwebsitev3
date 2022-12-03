from flask import Blueprint, request, render_template

guide = Blueprint("guide", __name__)

@guide.route("/api/guides/add")
def add_guide():
    data = request.get_json()
    