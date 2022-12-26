from flask import request, Blueprint

social_post = Blueprint("social_post", __name__)

@social_post.route("/api/social/add")
def add_social_thing():
    pass