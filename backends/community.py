from socket import IP_DEFAULT_MULTICAST_TTL, IP_DROP_MEMBERSHIP
from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from flask_login import current_user, login_required
from .models import Post, Tag, User, Notifications, Awnser, Postcomment
import math
# from . import app

community = Blueprint("community", __name__)

@community.route("/community")
def community_posts():
    posts = Post.query.order_by(Post.views)[::-1]
    return render_template("communtiy.html", posts=posts)
    
@community.route("/api/community/add", methods=["POST"])
def community_add_json():
    data = request.get_json()
    title = data["title"].replace(" ", "-")
    content = data["content"]
    user_id = data["userid"]
    # userx = db.session.query(User).filter(User.name == user).first()
    # if userx:
    #     user_id = userx.id
    # user_id = 1
    new_post = Post(title=title, content=content, user_id=user_id)
    for tag in data["tags"]:
        present = Tag.query.filter_by(name=tag).first()
        if present:
            present.posts.append(new_post)
        else:
            new_tag = Tag(name=Tag)
            new_tag.posts.append(new_post)
            db.session.add(new_tag)
    
    db.session.add(new_post)
    db.session.commit()
    post_id = getattr(new_post, 'id')
    return jsonify({"id": post_id})

@login_required
@community.route('/community/viewaddd')
def community_viewadd():
    title = request.form["title"].replace(" ", "-")
    user_id = current_user.id
    content = request.form["content"]
    tags = request.form["tags"].replace(" ", "-")

@login_required
@community.route("/community/viewadd", methods=["GET", "POST"])
def view_add_community():
    if request.method == "POST":
        title = request.form.get("title").replace(" ","-")
        user_id = current_user.id
        content = request.form.get("content")
        tags = request.form.get("tags").split(" ")
        new_post = Post(title=title, user_id=user_id, content=content)
        text_users = f"<a href='/user/views/{user_id}'>{current_user.name}</a> posted <a href='/community/view/{title}'>{title}</a>"
        users = []
        for tag in tags:
            present = Tag.query.filter_by(name=tag).first()
            if present:
                present.posts.append(new_post)
                followers = present.followers
                for follower in followers:
                    if follower.id not in users:
                        users.append(follower.id)
            else:
                new_tag = Tag(name=tag)
                new_tag.posts.append(new_post)
                db.session.add(new_tag)
            
        db.session.add(new_post)
        db.session.commit()
        post_id = getattr(new_post, "title")
        text = f"<p>you created a new post at <a href='/community/{post_id}'>{post_id}</a></p>"
        x = Notifications(user_id=user_id, text=text)
        
        for user in users:
            notification = Notifications(user_id=user, text=text_users)
            db.session.add(notification)
            
        db.session.add(x)
        db.session.commit()
        return redirect(f"/community/view/{post_id}")
    else:
        return render_template("communityadd.html")

@community.route("/community/view/<title>")
def view_all_community(title):
    post = Post.query.filter_by(title=title).first()
    tags = [tag.name for tag in post.tags]
    title = post.title
    user_id = post.user_id
    content = post.content
    awnsers = post.awnsers
    user = User.query.filter_by(id=user_id).first()
    user_name = user.name
    id = post.id
    dislikes = post.dislikes
    likes = post.likes
    created_at = post.created_at
    views = post.views
    post.views += 1
    comments = post.comments
    db.session.commit()
    return render_template("post.html", tags=tags, content=content, views=views, likes=likes, user_name=user_name, user_id=user_id, dislikes=dislikes, created_at=created_at, title=title, id=id, awnsers=awnsers, comments=comments)

@community.route("/community/views/<id>")
def redirect_to_actual_post(id):
    post = Post.query.filter_by(id=id).first()
    title = post.title
    return redirect(f"/community/view/{title}")

@community.route("/community/tags/<name>")
def communtiy_tags(name):
    tag = Tag.query.filter_by(name=name).first()
    posts = list(tag.posts)
    words = len([i.content.split() for i in posts])
    things = len(posts)
    time_to_read = (math.floor(words/200) + 1)
    avwords = words/things
    avtime = time_to_read/things
    id = tag.id
    if current_user.is_authenticated:
        following = current_user.following
        if tag in following:
            return render_template("tagblogs.html", blogs=posts, things=things, words=words, time_to_read=time_to_read, avwords=avwords, avtime=avtime, post=True, showf=False, unfollowf=True, id=id)
        else:
            return render_template("tagblogs.html", blogs=posts, things=things, words=words, time_to_read=time_to_read, avwords=avwords, avtime=avtime, post=True, showf=True, unfollowf=False, id=id)
    else:
        return render_template("tagblogs.html", blogs=posts, things=things, words=words, time_to_read=time_to_read, avwords=avwords, avtime=avtime, post=True, showf=False, unfollowf=False, id=id)    
    

@community.route('/community/addlike/<name>')
def add_like_community(name):
    post = Post.query.filter_by(title=name).first()
    post.likes += 1
    post.views -= 1
    user = User.query.filter_by(id=post.user_id).first()
    user.points += 1
    db.session.commit()
    return redirect(f"/community/view/{name}")

@community.route('/community/adddislike/<name>')
def add_dislike_community(name):
    post = Post.query.filter_by(title=name).first()
    post.dislikes += 1
    post.views -= 1
    user = User.query.filter_by(id=post.user_id).first()
    user.points -= 1
    db.session.commit()
    return redirect(f"/community/view/{name}")

@login_required
@community.route("/community/add/awnser/<id>", methods=["POST"])
def add_awnser_tp_post(id):
    user_id = current_user.id
    post_id = id
    title = request.form["title"]
    content = request.form["content"]
    author = request.form["author"]
    new_awnser = Awnser(user_id=user_id, post_id=post_id, title=title, content=content, author=author)
    db.session.add(new_awnser)
    db.session.commit()
    post = Post.query.filter_by(id=id).first()
    post_title = post.title
    text = f"<p>you created an awnser at <a href='/community/view/{post_title}'>{post_title}</a> called {title}</p>"
    notification = Notifications(text=text, user_id=user_id)
    db.session.add(notification)
    db.session.commit()
    return redirect(f'/community/view/{post_title}')

@login_required
@community.route("/user/tags/add/<id>")
def user_follow_tag(id):
    tag = Tag.query.filter_by(id=id).first()
    user = current_user
    if user not in tag.followers:
        tag.followers.append(user)
        text = f"<p>You are now following <a href='/blogs/tags/{tag.name}'>{tag.name}</a></p>"
        notification = Notifications(user_id=user.id, text=text)
        db.session.add(notification)
        db.session.commit()
        next = request.args.get("next", default="/dashboard")
        return redirect(next)


@login_required
@community.route("/user/tags/delete/<id>")
def user_unfollow_tag(id):
    tag = Tag.query.filter_by(id=id).first()
    user = current_user    
    tag.followers.remove(user)
    text = f"<p>You are no longer following <a href='/blogs/tags/{tag.name}'>{tag.name}</a></p>"
    notification = Notifications(user_id=user.id, text=text)
    db.session.add(notification)
    db.session.commit()
    next = request.args.get("next", default="/dashboard")
    return redirect(next)

@login_required
@community.route("/community/add/comment/post", methods=["POST"])
def community_add_comment():
    data = request.get_json()
    text = data["text"]
    author = current_user.name
    post_id = data["post_id"]
    parent = data["parent_id"]
    if parent == "":
        parent = None
    
    new = Postcomment(text=text, author=author, post_id=post_id, parent_id=parent)
    new.save()
    return jsonify({"message":new.level()})


@community.route("/api/community/add/comment/post", methods=["POST"])
def api_community_add_comment_to_post():
    data = request.get_json()
    text = data["text"]
    author = data["author"]
    post_id = data["post_id"]
    parent = data["parent_id"]
    new = Postcomment(text=text, author=author, post_id=post_id, parent_id=parent)
    new.save()
    return jsonify({"message": new.level()})
    

# app.register_blueprint(community, url_prefix="/")