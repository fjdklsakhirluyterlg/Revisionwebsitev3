import click
from flask import Blueprint

cli = Blueprint("cli", __name__, cli_group=None)

@bp.cli.command('create')
@click.argument('name')
def create(name):
    print(name)