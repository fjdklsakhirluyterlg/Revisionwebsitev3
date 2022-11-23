from backends.models import ScamPhone
from flask import Blueprint, request, render_template

scammer = Blueprint("scammer", __name__)

@scammer.route("/scams/support/add")
def add_scam():
    pass