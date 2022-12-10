from flask import Blueprint, request
from backends.models import Guide

guide_utils = Blueprint("guide_utils", __name__)

@guide_utils.route("/api/guides/fork", methods=["POST"])
def fork_guide_thing():
    data = request.get_json()
    guide_id = data["id"]
    user_id = data["user_id"]
    