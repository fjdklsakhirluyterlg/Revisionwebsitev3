from backends.models import ScamPhone
from flask import Blueprint, request, render_template

scammer = Blueprint("scammer", __name__)