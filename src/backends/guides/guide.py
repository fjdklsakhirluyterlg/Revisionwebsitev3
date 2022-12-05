from flask import Blueprint, request, render_template
from backends.models import Guide, ImageGuide, Tag
from backends import db
from werkzeug.utils import secure_filename

guide = Blueprint("guide", __name__)

@guide.route("/api/guides/add", methods=["POST"])
def add_guide():
    data = request.get_json()
    content = data["content"]
    user_id = data["user_id"]
    new = Guide(content=content, user_id=user_id)
    db.session.add(new)
    db.session.commit()
    id = getattr(new, "id")
    for file in request.files:
        filename = secure_filename(file.filename)
        new_image = ImageGuide(guide_id=id, name=filename)
        db.session.add(new_image)
    for tag in data["tags"]:
        tag = Tag.query.filter_by(name=tag).first()
        tag.guides.append(new)
    
    db.session.commit()

    return {"id":id}

@guide.route("/api/guide/all")
def api_guide_all():
    dict = {}
    guides = Guide.query.all()
    for guide in guides:
        dict[guide.id] = {"content":guide.content}

    return dict

@guide.route("/api/guide/view/<id>")
def return_singel_guide_thign():
    pass