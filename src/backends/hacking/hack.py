from flask import Blueprint, request 

hack = Blueprint("hack", __name__)

@hack.route("/hack/signup")
def signup():
    