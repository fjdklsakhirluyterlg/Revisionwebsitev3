from flask import Blueprint, render_template, request

news = Blueprint("news", __name__)

@news.route("/news/source/<name>")
def return_news_source(name):
    pass