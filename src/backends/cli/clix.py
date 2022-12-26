import click
from flask import Blueprint
from backends import db
from backends.models import User, Blod
from werkzeug.security import generate_password_hash, check_password_hash
from backends.auth import login, make_security_key
from flask_login import logout_user, login_user
from backends.utilities.imagecompressor import clear_revisionwebs

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
def man_pages_for_app(feature):
    if feature == "user":
        out = """
        The user feautre allows people to do many services and access other feautures 

        Users have access to the 

        - shop
        - commenting
        - notes
        - chat
        - bookmarks
        """
        print(out)

@clix.cli.command("login")
@click.argument("name")
def cli_login_user(name):
    user = User.query.filter_by(name=name).first()
    login_user(user, remember=True)
    print("logged in")

@clix.cli.command("sitemap")
def sitemap():
    pass

@clix.cli.command("add-blog")
@click.argument("title")
@clicj.argument("content")
def add_feature_to_database(title, content):
    new = Blog(title=title, content=content)
    
@clix.cli.command("clean images")
def clean_all_images():
    print("cleaning")
    clean_revisionwebs()
    print("cleaned")

@clix.cli.command("show users")
def show_users_stuff():
    users = User.query.all()
    