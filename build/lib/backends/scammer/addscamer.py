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

@scammer.route("/api/scammer/all")
def scammer_all_api():
    email - ScamPhone.query.all()
    phone = ScamEmail.query.all()
    dict = {}
    for em in email:
        dict[em.id] = []
