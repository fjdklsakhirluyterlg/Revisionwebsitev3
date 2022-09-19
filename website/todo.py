from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from .models import Todo
from . import app

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

@todo.route("/api/todo/add")
def api_add_todo():
    x = request.args.get("title")
    new_todo = Todo(title=x, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(message="worked")

@todo.route("/api/todo/delete")
def api_delete_todo():
    id = request.args.get("id")
    todo = db.session.query(Todo).filter(Todo.id == id).first()
    db.session.delete(todo)
    db.session.commit()
    return ""

@todo.route("/api/todo/")
@todo.route("/api/todo/view")
def api_todo_view():
    x = db.session.query(Todo).all()
    dict = {}
    for i in x:
        dict[f"{i.id}"] = [i.title, i.complete]
    return dict

app.register_blueprint(todo, url_prefix='/')