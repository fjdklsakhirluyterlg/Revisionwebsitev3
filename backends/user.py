from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from .models import User
from flask_login import current_user, login_required
from .auth import mank_random_long_id, validate_user_with_email
from .models import Blog, Notifications, Tag, Post
from werkzeug.security import generate_password_hash, check_password_hash
from .blogs import blogs_related_to_blog, related_tags_thingy
from .community import find_user_related_posts, posts_related_to_post
# from . import app

user = Blueprint("user", __name__)

@login_required    
@user.route("/dashboard")
def dashboard():
    try:
        usern = current_user
        name = usern.name
        email = usern.email
        joined = usern.timestamp
        id = usern.id
        points = usern.points
        comments = usern.comments
        l = []
        for comment in comments:
            x = comment.blog_id
            blog = db.session.query(Blog).filter(Blog.id == x).first()
            l.userend(blog)
        
        notifications = db.session.query(Notifications).filter(Notifications.user_id == id).all()[::-1]
        bookmarks = usern.bookmarks
        blog_bookmarks = []
        for bookmark in bookmarks:
            bookmark_blog_id = bookmark.blog_id
            hog = Blog.query.filter_by(id=bookmark_blog_id).first()
            blog_bookmarks.userend(hog.title)
            
        posts = usern.posts
        awnsers = usern.awnsers
        notes = usern.notes
        if usern.validated == False:
            ask = True
        else:
            ask = False
        
            
        return render_template('dashboard.html', name=name, email=email, joined=joined, id=id, comments=zip(comments, l), points=points, ask=ask, notifications=notifications, bookmarks=zip(bookmarks, blog_bookmarks), posts=posts, awnsers=awnsers, notes=notes)  
    except:
        return redirect("/login")

@user.route("/user/notification/markasread/<id>")
def mark_notification_as_read(id):
    notification = db.session.query(Notifications).filter(Notifications.id == id).first()
    notification.read = True
    db.session.commit()
    return redirect("/dashboard")

@login_required
@user.route("/user/notification/allread/<id>")
def mark_all_notification_as_read(id):
    user = db.session.query(User).filter(User.id == id).first()
    notifications = user.notifications
    for i in notifications:
        i.read = True
    
    db.session.commit()
    return redirect("/dashboard")

@login_required
@user.route("/users/edit/<id>", methods=["POST", "GET"])
def edit_user(id):
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        user = db.session.query(User).filter(User.id == id).first()
        user.name = name
        user.email = email
        user.validated = False
        new = Notifications(text="You changed your settings!", user_id=id)
        db.session.add(new)
        db.session.commit()
        return redirect(f"/dashboard")
    else:
        id = current_user.id
        name = current_user.name
        email = current_user.email
        return render_template("edituser.html", id=id, name=name, email=email)

@user.route("/users/delete/<id>")
def delete_user(id):
    user = db.session.query(User).filter(User.id == id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect("/login")

@user.route("/users/view/<int:id>")
def view_user(id):
    user = db.session.query(User).filter(User.id == id).first()
    comments = user.comments
    name = user.name
    l = []
    for comment in comments:
        x = comment.blog_id
        blog = db.session.query(Blog).filter(Blog.id == x).first()
        l.userend(blog) 
    
    posts = user.posts
    awnsers = user.awnsers
    
    if current_user.is_authenticated and id != current_user.id:
        if current_user.is_following(user):
            return render_template("viewuser.html", name=name, comments=zip(comments, l), posts=posts, awnsers=awnsers, show=True, id=id, follow=False)
        return render_template("viewuser.html", name=name, comments=zip(comments, l), posts=posts, awnsers=awnsers, show=True, id=id, follow=True)
    return render_template("viewuser.html", name=name, comments=zip(comments, l), posts=posts, awnsers=awnsers, show=False, id=id, follow=False)

@login_required
@user.route("/user/validate/<securitykey>")
def validate_user(securitykey):
    user = db.session.query(User).filter(User.security_key == securitykey).first()
    if user.id == current_user.id:
        user.validated = True
        db.session.commit()
        return redirect("/dashboard")
    else:
        return redirect("/user/settings/validationerror")

@login_required
@user.route("/user/settings/validationerror")
def set_new_security_key():
    try:
        security_key = mank_random_long_id(64)
        current_user.security_key = security_key
        db.session.commit()
        validate_user_with_email(address=current_user.email, securitykey=security_key, name=current_user.name)
        return "please check your email again"
    except:
        return "sorry there is an error somewhere, please email me directly at banerjee.armaan@gmail.com so i can try and fix the error. I am very sorry about this error. Please try again later if possible and please only have 1 account per browser window, sorry about that but thats how the cookies work"

@login_required
@user.route("/user/settings/disnewsletter")
def disable_newsletter_for_user():
    current_user.newsletter = False
    db.session.commit()
    return redirect("/dashboard")

@login_required
@user.route("/user/edit/changepassword", methods=["POST", "GET"])
def change_password_for_user():
    if request.method == "POST":
        current = request.form["current"]
        if check_password_hash(current, current_user.password):
            new = request.form["new"]
            current_user.password = generate_password_hash(new, method='sha256')
            db.session.commit()
            return redirect("/dashboard")
        else:
            return render_template("changepassword.html", msg="invalid credentials")
    else:
        return render_template("changepassword.html")
    
@user.route("/user/rankings")
def ranking_of_users():
    limit = request.args.get("limit", default=10)
    users = User.query.order_by(User.points)[::-1][(limit - 1):limit]
    return render_template("userrankings.html", users=users)

@login_required
@user.route("/user/settings/mod")
def become_mod():
    points = current_user.points
    if points >= 1:
        current_user.mod = True
    
    db.session.commit()
    return redirect('/dashboard')

@login_required
@user.route('/user/settings/superuser')
def become_super_user():
    points = current_user.points
    if points >= 1:
        current_user.superuser = True
        current_user.mod = True
    
    db.session.commit()
    return redirect("/dashboard")

@login_required
@user.route("/user/home")
def user_home():
    user = current_user
    following = user.following
    blogs = []
    blogids = []
    for tag in following:
        blogx = tag.blogs_associated
        for blog in blogx:
            if blog.title not in blogs:
                blogs.append(blog.title)
                blogids.append(blog.id)
    
    ids = [tag.blogs_associated for tag in following]
    
    
    # otherblogs = Blog.query.order_by(Blog.views)
    # otherblogt = [i.title for i in otherblogs]
    # x = otherblogt[:diff]
    # return jsonify({"following": blogs, "filler": x})
    othertags = find_user_related_tags()
    otherblogs = []
    for blog in blogids:
        otherblogs.extend(list(blogs_related_to_blog(blog).keys()))
    

    tag_blogs = []
    for tagt in othertags:
        tagtt = Tag.query.filter_by(name=tagt).first()
        blogggs = tagtt.blogs_associated
        for b in blogggs:
            if b.id not in blogids or otherblogs:
                tag_blogs.append(b.title)

    tagsxx = user.following
    tagnames = [tagsxxx.name for tagsxxx in tagsxx]
    
    posts = find_user_related_posts()
    postnames = posts["names"]
    postids = posts["ids"]

    recposts = []
    for postid in postids:
        postsrecommended = posts_related_to_post(postid).keys()
        for postrecomnd in postsrecommended:
            if postrecomnd not in postnames:
                recposts.append(postrecomnd)

    
    user_followed_posts = []
    followers = user.followers
    for folls in followed:
        posts = folls.posts
        for zsy in posts:
            user_followed_posts.append(zsy.name)

    return jsonify({"following": blogs, "reccomended": list(set(otherblogs)), "tags reccomended": othertags, "tag_blogs": tag_blogs, "tags":tagnames, "posts":postnames, "recomended_posts":recposts, "user_followed_posts":user_followed_posts})

@login_required
@user.route("/find/related/tags")
def find_user_related_tags():
    tags = current_user.following
    ids = [tag.id for tag in tags]
    names = [tag.name for tag in tags]
    list = []
    dictx = {}
    for id in ids:
        x = related_tags_thingy(id)
        sort_by_value = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))
        dictx = dictx | sort_by_value   
        list.append(sort_by_value)
    
    # return jsonify(list)   
    sort = dict(sorted(dictx.items(), key=lambda item: item[1], reverse=True))
    # for name in names:
    #     if name in sort:
    #         del sort[name]
    return sort 

@user.route("/follow/user", methods=["POST"])
def follow_user():
    data = request.get_json()
    current_user = data["current_user"]
    followed = data["followed"]
    user = User.query.filter_by(id=followed).first()
    current = User.query.filter_by(id=current_user).first()
    current.follow(user)
    db.session.commit()
    text = f"You are now following {user.name}"
    new_notification = Notifications(user_id=current.id, text=text)
    db.session.add(new_notification)
    db.session.commit()
    return {"msg":"following"}

@user.route("/unfollow/user", methods=["POST"])
def unfollow_user():
    data = request.get_json()
    current_user = data["current_user"]
    followed = data["followed"]
    user = User.query.filter_by(id=followed).first()
    current = User.query.filter_by(id=current_user).first()
    current.unfollow(user)
    db.session.commit()
    text = f"You are no longer following {user.name}"
    new_notification = Notifications(user_id=current.id, text=text)
    db.session.add(new_notification)
    db.session.commit()
    return {"msg":"unfollowed"}

@user.route("/api/user/info")
def show_me_user_info_thingy():
    id = request.args.get("id")
    dict = {}
    user = User.query.filter_by(id=id).first()
    dict["key"] = user.security_key
    return dict

@user.route("/api/user/followers/<id>")
def user_followers_api_test(id):
    user = User.query.filter_by(id=id).first()
    followers = [i.name for i in user.followers]
    return {"amount":followers}

# app.register_blueprint(user, url_prefix="/")