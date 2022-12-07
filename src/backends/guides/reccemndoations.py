from flask import Blueprint, request
from backends.models import Guide

recomendation_guide = Blueprint("recomendation_guide", __name__)

@recomendation_guide.route("/api/reccomend/<id>")
def reccomnd_guide_on_id(id):
    guide = Guide.query.filter_by(id=id).first()
