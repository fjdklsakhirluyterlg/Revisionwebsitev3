from flask import Blueprint, request

guide_utils = Blueprint("guide_utils", __name__)

@guide_utils.route("/api/guides/fork", methods=["POST"])
def fork_guide_thing():
    pass