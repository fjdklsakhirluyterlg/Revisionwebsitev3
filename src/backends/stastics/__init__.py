import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from backends import create_app

def new_app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    