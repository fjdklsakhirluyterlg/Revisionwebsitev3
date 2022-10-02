
from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from .models import Blog, User, Comment, Replies, User, Tag, Post, Awnser
from sqlalchemy import or_
# from . import app

search = Blueprint("search", __name__)

@search.route("/api/searchh")
def try_to_search_everything():
    query = request.args.get("q")
    blogs = db.session.query(Blog).all()
    users = db.session.query(User).all()
    comments = db.session.query(Comment).all()
    replies = db.session.query(Replies).all()
    titles = (blog.title for blog in blogs)
    contents = (blog.content for blog in blogs)
    names = (user.name for user in users)
    comment_texts = (comment.text for comment in comments)
    reply_texts = (reply.text for reply in replies)
    result = ""
    if query in titles:
        blog = Blog.query.filter_by(title=query).all()
        result += f"the search matches some blog title"
    if query in comments:
        comment = Comment.query.filter_by(text=query).first()
        result += "the search matches some comments"
    if query in names:
        # user = User.query.filter_by(name-query).first()
        result += f"The search matches some users"
    if query in contents:
        thing = Blog.query.filter_by()

@search.route("/api/search/tags")
def search_tags_thing():
    q = request.args.get("q")
    q = q.strip()
    result = Tag.query.filter(Tag.name.like(f"%{q}%")).all()
    things = [res.name for res in result]    
    return jsonify(things)

@search.route("/api/search")
def search_all_the_things():
    q = request.args.get("q")
    q.strip()
    resblogs = Blog.query.filter(or_(Blog.title.like(f"%{q}%"), Blog.content.like(f"%{q}%"), Blog.created_at.like(f"%{q}%"), Blog.views.like(f"%{q}%"))).all()
    blogs = [blog.title for blog in resblogs]
    rescomments = Comment.query.filter(or_(Comment.text.like(f"%{q}%"), Comment.timestamp.like(f"%{q}%"))).all()
    comments = [comment.text for comment in rescomments]
    resrelpies = Replies.query.filter(or_(Replies.text.like(f"%{q}%"), Replies.timestamp.like(f"%{q}%"))).all()
    replies = [replies.text for replies in resrelpies]
    restags = Tag.query.filter(or_(Tag.name.like(f"%{q}%"))).all()
    tags = [tag.name for tag in restags]
    resposts = Post.query.filter(or_(Post.title.like(f"%{q}%"), Post.content.like(f"%{q}%"), Post.views.like(f"%{q}%"), Post.created_at.like(f"%{q}%")))
    posts = [post.title for post in resposts]
    resusers = User.query.filter(or_(User.name.like(f"%{q}%"), User.timestamp.like(f"%{q}%")))
    users = [user.name for user in resusers]
    dict = {"blogs": blogs, "comments": comments, "replies": replies, "tags": tags, "posts": posts, "users": users}
    # return jsonify(blogs, comments, replies, tags, posts, users)
    return dict

@search.route("/search")
def search_wiht_template():
    return render_template("search.html")

@search.route("/search/better")
def better_search():
    q = request.args.get("q")
    q.strip()
    resblogs = Blog.query.filter(or_(Blog.title.like(f"%{q}%"), Blog.content.like(f"%{q}%"), Blog.created_at.like(f"%{q}%"), Blog.views.like(f"%{q}%"))).all()
    blogs = [blog.title for blog in resblogs]
    rescomments = Comment.query.filter(or_(Comment.text.like(f"%{q}%"), Comment.timestamp.like(f"%{q}%"))).all()
    comments = [comment.text for comment in rescomments]
    resrelpies = Replies.query.filter(or_(Replies.text.like(f"%{q}%"), Replies.timestamp.like(f"%{q}%"))).all()
    replies = [replies.text for replies in resrelpies]
    restags = Tag.query.filter(or_(Tag.name.like(f"%{q}%"))).all()
    tags = [tag.name for tag in restags]
    resposts = Post.query.filter(or_(Post.title.like(f"%{q}%"), Post.content.like(f"%{q}%"), Post.views.like(f"%{q}%"), Post.created_at.like(f"%{q}%")))
    posts = [post.title for post in resposts]
    resusers = User.query.filter(or_(User.name.like(f"%{q}%"), User.timestamp.like(f"%{q}%")))
    users = [user.name for user in resusers]
    resawnsers = Awnser.query.filter(or_(Awnser.title.like(f"%{q}%")))
    return render_template("bettersearch.html", blogs=resblogs, tags=restags, comments=rescomments, posts=resposts, replies=resrelpies, users=resusers)

# app.register_blueprint(search, url_prefix="/")