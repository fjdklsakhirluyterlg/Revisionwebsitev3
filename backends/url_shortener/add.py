from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from backends.models import urlshortner
from backends import db

add_url = Blueprint("add_url", __name__)

@add_url.route("/api/urls/shortner/test")
def test_thingy():
    return "here"

@add_url.route('/api/urls/shortner/add')
def add_url_to_shortenere():
    pass