import click
from flask import Blueprint
from backends import db
from backends.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from backends.auth import make_security_key

clix = Blueprint("cli", __name__, cli_group=None)

@clix.cli.command('create')
@click.argument('name')
def create(name):
    email = "admin@admin.com"
    new = User(name=name, email=email, password=generate_password_hash("password", method="sha256"), security_key=make_security_key())

@clix.cli.command("get")
@click.argument("users")
def get_useres(users):
    users = User.query.all()
    dict = {}
    for user in users:
        dict[user.id] = {"name":user.name, "email":user.email, "points":user.points}
    print(dict)