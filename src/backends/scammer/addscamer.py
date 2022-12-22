from backends.models import ScamPhone, ScamEmail
from flask import Blueprint, request, render_template

scammer = Blueprint("scammer", __name__)

@scammer.route("/scams/support/add")
def add_scam():
    data = request.get_json()
    type = data["type"]
    if type == "phone":
        telephone = data["telephone"]
        new = ScamPhone(telephone)
    elif type == "email":
        email = data["email"]
        new = ScamEmail(email)
    
    db.session.add(new)
