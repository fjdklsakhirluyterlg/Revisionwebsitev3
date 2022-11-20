import click
from flask import Blueprint
from backends import db
from backends.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from backends.auth import login, make_security_key
from flask_login import logout_user, login_user

clix = Blueprint("cli", __name__, cli_group=None)

@clix.cli.command('create')
@click.argument('name')
def create(name):
    email = "admin@admin.com"
    new = User(name=name, email=email, password=generate_password_hash("password", method="sha256"), security_key=make_security_key())
    db.session.add(new)
    db.session.commit()

@clix.cli.command("get")
@click.argument("users")
def get_useres(users):
    users = User.query.all()
    dict = {}
    for user in users:
        dict[user.id] = {"name":user.name, "email":user.email, "points":user.points}
    print(dict)

@clix.cli.command("man")
@click.argument("feature")
def man_pages_for_app():
    pass

@clix.cli.command("login")
@click.argument("name")
def cli_login_user(name):
    user = User.query.filter_by(name=name).first()
    login_user(user, remember=True)
    print("logged in")