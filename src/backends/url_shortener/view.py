from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from backends.models import Urlshortner
view_url = Blueprint("view_url", __name__)

@view_url.route("/urls/<name>")
def view_url_thing(name):
    url = Urlshortner.query.filter_by(id=name).first()
    url.views += 1
    return f"""
    <head><script>window.location.href="{url}"</script></head>
    """
