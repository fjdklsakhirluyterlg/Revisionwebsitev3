import click
from flask import Blueprint
from backends import db
from backends.models import User
from werkzeug.security import generate_password_hash, check_password_hash

clix = Blueprint("cli", __name__, cli_group=None)

@clix.cli.command('create')
@click.argument('name')
def create(name):
    email = "admin@admin.com"

@clix.cli.command("get")
@click.argument("users")
def get_useres(users):
    users = User.query.all()
    dict = {}
    for user in users:
        dict[user.id] = {"name":user.name, "email":user.email, "points":user.points}
    print(dict)