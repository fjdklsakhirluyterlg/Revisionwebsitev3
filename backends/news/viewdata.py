from flask import Blueprint, render_template, request
from getdata import *

news = Blueprint("news", __name__)

@news.route("/news/source/<name>")
def return_news_source(name):
    if name == "bbc":
        results = get_bbc_news()