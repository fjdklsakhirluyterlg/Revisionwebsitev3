from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from .models import Readinglist
from . import app

book = Blueprint("book", __name__)

@book.route('/books')
def get_books():
    listx = db.session.query(Readinglist).all()
    return render_template("books.html", listy=listx)

@book.route('/books/add')
def add_books():
    titlen = request.form.get("booktitle")
    authorn = request.form.get("bookauthor")
    summaryn = request.form.get("booksummary")
    pages = request.form.get("pages", default = 0)
    newbook = Readinglist(list=titlen, summary=summaryn, author=authorn, pages=pages)
    db.session.add(newbook)
    db.session.commit()
    return redirect(url_for("get_books"))

@book.route("/books/delete/<int:bookid>")
def deletebook(bookid):
    book = db.session.query(Readinglist).filter(Readinglist.id == bookid).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("get_books"))

@book.route("/api/readinglist/add")
def api_add_readinglist():
    list = request.args.get("name", default="test")
    author = request.args.get("author", default="me")
    summary = request.args.get("summary", default="TEST")
    pages = request.args.get("pages", default=10)
    rating = request.args.get("rating", default=4.0)
    x = Readinglist(list=list, author=author, summary=summary, pages=pages, rating=rating)
    db.session.add(x)
    db.session.commit()
    return jsonify(message="worked")

@book.route("/api/readinglist")
@book.route("/api/readinglist/view")
def api_readinglisst_view():
    x = db.session.query(Readinglist).all()
    dict = {}
    for i in x:
        dict[i.id] = [i.list, i.author, i.summary, i.pages, i.rating]
    
    return dict

@book.route("/api/readinglist/delete")
def api_readinglist_delete():
    id = request.args.get("id")
    book = db.session.query(Readinglist).filter(Readinglist.id == id).first()
    db.session.delete(book)
    db.session.commit()
    return jsonify(message="worked")

@book.route("/api/readinglist/deletebook")
def api_readinglist_delete_book():
    x = request.args.get("name")
    book = db.session.query(Readinglist).filter(Readinglist.list == x).first()
    db.session.delete(book)
    db.session.commit()
    return jsonify(message="worked")

@book.route("/api/readinglist/cancel")
def api_readinglist_cancel():
    author = request.args.get("author")
    books = db.session.query(Readinglist).filter(Readinglist.author == author).all()
    for i in books:
        db.session.delete(i.id)
    db.session.commit()
    return jsonify(message="you canceleed a guy")

@book.route("/api/readinglist/search")
def api_readinglist_search():
    p = request.args.get("p", default="list")
    q = request.args.get("q", default="test")
    if p == "title":
        p = "list"
    
    x = ""
    if p == "author":
        x = db.session.query(Readinglist).filter(Readinglist.author == q).all()
    elif p == "rating":
        x = db.session.query(Readinglist).filter(Readinglist.rating == q).all()
    elif p == "pages":
        x = db.session.query(Readinglist).filter(Readinglist.pages == q).all()
    elif p == "title" or p == "list":
        x = db.session.query(Readinglist).filter(Readinglist.list == q).all()
    
    dict = {}
    
    for i in x:
        dict[i.id] = i.list
    
    return dict

app.register_blueprint(book, url_prefix="/")