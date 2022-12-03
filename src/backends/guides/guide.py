from flask import Blueprint, request, render_template
from backends.models import Guide
from backends import db
guide = Blueprint("guide", __name__)

@guide.route("/api/guides/add", methods=["POST"])
def add_guide():
    data = request.get_json()
    content = data["content"]
    user_id = data["user_id"]
    new = Guide(content=content, user_id=user_id)
    db.session.add(new)
    db.session.commit()