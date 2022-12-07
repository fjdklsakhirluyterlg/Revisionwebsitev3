from flask import Blueprint, request
from backends.models import Guide, Tag
from flask_login import current_user, login_required

recomendation_guide = Blueprint("recomendation_guide", __name__)

@recomendation_guide.route("/api/reccomend/<id>")
def reccomnd_guide_on_id(id):
    guide = Guide.query.filter_by(id=id).first()
    tags = guide.tags
    dict = {}
    for tag in tags:
        guides = tag.guides
        for g in guides:
            if dict[g.id]:
                dict[g.id] += 1
            else:
                dict[g.id] = 1
    
    return dict

@recomendation_guide.route("/api/guide/tag/<id>")
def guide_tag(id):
    tag = Tag.query.filter_by(id=id).first()
    guides = tag.guides

@login_required
@recomendation_guide.route("/api/reccomend/guide/user")
def reccomend_for_current_user():
    following = current_user.following
    dict = {}

