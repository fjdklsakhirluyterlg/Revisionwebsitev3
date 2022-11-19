import click
from flask import Blueprint
from backends import db
from backends.models import User

clix = Blueprint("cli", __name__, cli_group=None)

@clix.cli.command('create')
@click.argument('name')
def create(name):
    print(name)