from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from .models import Todo

todo = Blueprint('todo', __name__)

@todo.get('/todo')
def show_todo():
    todo_list = db.session.query(Todo).all()
    return render_template("todo.html", todo_list=todo_list)

@todo.post("/todo/add")
def todo_add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("show_todo"))

@todo.get("/todo/update/<int:todo_id>")
def update(todo_id):
    # todo = Todo.query.filter_by(id=todo_id).first()
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("show_todo"))

@todo.get("/todo/delete/<int:todo_id>")
def deletet(todo_id):
    # todo = Todo.query.filter_by(id=todo_id).first()
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("show_todo"))