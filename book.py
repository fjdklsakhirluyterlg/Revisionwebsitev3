from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from .models import Readinglist

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