from flask import Blueprint, request

recomendation_guide = Blueprint("recomendation_guide", __name__)

@recomendation_guide.route("/api/reccomend/<id>")
def reccomnd_guide_on_id():
    pass
