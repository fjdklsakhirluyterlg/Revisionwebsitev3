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
    title = data["title"]
    new = Guide(content=content, user_id=user_id, title=title)
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
    guide = Guide.query.filter_by(id=id).first()
    content = guide.content 
    dict = {}
    dict[guide.id] = content

@guide.route("/api/guide/delete/<id>")
def delete_guide_from_id():
    guide = Guide.query.filter_by(id=id).first()
    db.session.delete(guide)

@guide.route("/api/guide/edit/<id>", methods=["POST"])
def edit_id_thing():
    data = request.get_json()
    content = data["content"]
    id = data["id"]
    guide = Guide.query.filter_by(id=id).first()
    guide.content = content
    db.session.commit()
