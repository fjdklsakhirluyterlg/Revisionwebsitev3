from flask import Blueprint, request
from backends.models import Guide
from backends import db

guide_utils = Blueprint("guide_utils", __name__)

@guide_utils.route("/api/guides/fork", methods=["POST"])
def fork_guide_thing():
    data = request.get_json()
    guide_id = data["id"]
    user_id = data["user_id"]
    guide = Guide.query.filter_by(id=guide_id).first()
    new = Guide(title=guide.title, content=guide.content, user_id=user_id)
    db.session.add(new)
    db.session.commit()

@guide_utils.route("/api/guides/like/<id>")
def like_guide(id):
    pass