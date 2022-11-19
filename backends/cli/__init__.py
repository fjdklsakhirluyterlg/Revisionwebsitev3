import click
from flask import Blueprint

clix = Blueprint("cli", __name__, cli_group=None)

@clix.cli.command('create')
@click.argument('name')
def create(name):
    print(name)