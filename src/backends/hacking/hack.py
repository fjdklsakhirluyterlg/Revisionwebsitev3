from flask import Blueprint, request 
from backends.hacking.write import check_if_database_has_data


hack = Blueprint("hack", __name__)

@hack.route("/hack/signup")
def signup():
    check_if_database_has_data()

@hack.route("/hack/ip/check")
def check_ip():
    pass