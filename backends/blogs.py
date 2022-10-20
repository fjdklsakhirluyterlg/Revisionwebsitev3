from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from . import db
from .models import Blog, Notifications, Post, Tag, tag_blog, Comment, Replies, User, Bookmark
from flask_login import current_user, login_required
import html, requests, math
from .functions import send_newsletter_with_flask
import markdown
# from . import app

blogs = Blueprint("blogs", __name__)

@blogs.route('/blogs/add',methods=["POST"])
def create_blog():
    data = request.get_json()
 
    new_blog=Blog(title=data["title"].replace(" ", "-"),content=data["content"],feature_image=data["feature_image"])
    users = []
    for tag in data["tags"]:
        present_tag=Tag.query.filter_by(name=tag).first()
        if(present_tag):
            present_tag.blogs_associated.append(new_blog)
            followers = present_tag.followers
            for follower in followers:
                if follower.id not in users:
                    users.append(follower.id)
            
        else:
            new_tag=Tag(name=tag)
            new_tag.blogs_associated.append(new_blog)
            db.session.add(new_tag)
            
    text = f"""<p><a href='/blogs/views/{data["title"]}'>{data["title"]}</a> was created"""
    for user in users:
        notification = Notifications(user_id=user, text=text)
        db.session.add(notification)    
    
    db.session.add(new_blog)
    db.session.commit()
 
    blog_id = getattr(new_blog, "id")
    return jsonify({"id": blog_id})


@blogs.route('/blogs',methods=["GET"])
def get_all_blogs():
    blogs = Blog.query.all()
    serialized_data = []
    for blog in blogs:
        serialized_data.append(blog.serialize)
 
    return jsonify(serialized_data)

@blogs.route('/blogs/<int:id>',methods=["GET"])
def get_single_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    serialized_blog = blog.serialize
    serialized_blog["tags"] = []
 
    for tag in blog.tags:
        serialized_blog["tags"].append(tag.serialize)
 
    return {"single_blog": serialized_blog}

@blogs.route('/blogs/update/<int:id>', methods=["POST"])
def update_blog(id):
    data = request.get_json()
    blog=Blog.query.filter_by(id=id).first_or_404()
 
    blog.title = data["title"]
    blog.content=data["content"]
    blog.feature_image=data["feature_image"]
 
    updated_blog = blog.serialize
 
    db.session.commit()
    return jsonify({"blog_id": blog.id})

@blogs.route('/blogs/delete/<int:id>')
def delete_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()
 
    return jsonify("Blog was deleted"),200

@blogs.route("/blogs/tags")
def view_tags():
    x = db.session.query(Tag).all()
    dict = {}
    for i in x:
        dict[i.id] = i.name
    
    return dict

@blogs.route("/blogs/tags/delete")
def delete_tags():
    id = request.args.get("id", default=1)
    tag = db.session.query(Tag).filter(Tag.id == id).first()
    db.session.delete(tag)
    db.session.commit()

@blogs.route("/blogs/tags/alll")
def view_tags_alll():
    x = db.session.query(Tag).all()
    dict = {}
    s = []
    for i in x:
        tagx = i.name
        blogs = db.session.query(Blog).all()
        for blog in blogs:
            serialized_blog = blog.serialize
            serialized_blog["tags"] = []
 
            for tag in blog.tags:
                serialized_blog["tags"].append(tag.serialize)
            
            s = []
            for i in range(len(serialized_blog["tags"])):
                if serialized_blog["tags"][i]["name"] == tagx:
                    s.append(serialized_blog["title"])
            # why dont you work?
            
        
        dict[tagx] = s
    
    return dict

@blogs.route("/blogs/tags/allll")
def view_tags_allll():
    tags = db.session.query(Tag).all()
    dict = {}
    for tag in tags:
        l = []
        blogs = db.session.query(Blog).all()
        for blog in blogs:
            if blog.tags == tag:
                l.append(blog)
        # l.append(n)
        
    return dict

@blogs.route("/blogs/related/<id>")
def blogs_related_to_blog(id):
    current = db.session.query(Blog).filter(Blog.id == id).first()
    tags = current.tags
    dict = {}
    blogs = Blog.query.order_by(Blog.views)
    for tag in tags:
        for blog in blogs:
            if tag in blog.tags:
                if blog.title in dict and blog.title != current.title:
                    dict[blog.title] += 1
                elif blog.title != current.title:
                    dict[blog.title] = 1
    
    # sorted_value_index = np.argsort(dict.values())
    # dictionary_keys = list(dict.keys())
    # sorted_dict = {dictionary_keys[i]: sorted(
    #     dict.values())[i] for i in range(len(dictionary_keys))}
    
    
    return dict

@blogs.route("/api/what/blogs")
def blog_what():
    x = blogs_related_to_blog(1)
    return jsonify(msg=f"{x}")
        
@blogs.route("/blogs/tags/all")
def view_tags_all():
    x = db.session.query(Tag).all()
    dict = {}
    for i in x:
        y = i.name
        blogs = db.session.query(Blog).all()
        n = []
        for blog in blogs:
            id = blog.id
            hhh = blog.title
            yyy = get_single_blog(id)
            zzz = yyy["single_blog"]["tags"]
            for pp in range(len(zzz)):
                aaa = zzz[pp]["name"]
                if aaa == y:
                    n.append(hhh)
            
        dict[y] = n
    
    return dict

@blogs.route("/tags/all")
def tag_definitive_all():
    tags = db.session.query(Tag).all()
    dict = {}
    for tag in tags:
        x = tag.blogs_associated
        y = tag.posts
        blog_name = [i.title for i in x]
        post_name = [i.title for i in y]
        dict[tag.name] = [blog_name, post_name], tag.id
    return dict
        
@blogs.route("/blogs/tags/single")
def view_tags_single():
    id = request.args.get("id")
    x = db.session.query(Tag).filter(Tag.id == id).first()
    y = x.name
    n = []
    dict = {}
    blogs = db.session.query(Blog).all()
    for blog in blogs:
            id = blog.id
            hhh = blog.title
            yyy = get_single_blog(id)
            zzz = yyy["single_blog"]["tags"]
            for pp in range(len(zzz)):
                aaa = zzz[pp]["name"]
                if aaa == y:
                    n.append(hhh)
    
    dict[y] = n
    return dict

@blogs.route("/blog/view/<id>")
def redirect_based_on_id(id):
    comment = request.args.get("c")
    blog = Blog.query.filter_by(id=id).first()
    return redirect(f"/blogs/views/{blog.title}#{comment}")
            
@blogs.route("/blogs/views/<title>")
def see_content_blog(title):
    x = db.session.query(Blog).filter(Blog.title == title).first()   
    contentx = (html.unescape(x.content)).replace("\r", "")
    content = contentx
    time = x.created_at
    title = x.title
    id = x.id
    likes = x.likes
    dislikes = x.dislikes
    words = len(x.content.split())
    read_time = (math.floor(words/200) + 1)
    y = get_single_blog(id)
    n = []
    z = y["single_blog"]["tags"]
    for i in range(len(z)):
        n.append(z[i]["name"])
    tags = n
    views = x.views
    x.views += 1
    db.session.commit()
    related = blogs_related_to_blog(id)
    rellist = []
    revli = []
    for key, value in related.items():
        rellist.append(key)
        revli.append(value)
    
    revli.sort(reverse=True)
    zippedli = zip(rellist, revli)
    actrel = [key for key, val in zippedli]

    current_bookmarks = [bookmark.blog_id for bookmark in current_user.bookmarks]
    bookmarked = True if id in current_bookmarks else False
    note = ""
    if bookmarked:
        bookmark = Bookmark.query.filter_by(blog_id=id).first()
        note += bookmark.note

    commentsx = []
    p = request.args.get("commentssort", default="likes")
    if p == "oldest":
        comments = db.session.query(Comment).all()
    elif p == "newest":
        comments = db.session.query(Comment).all()[::-1]
    elif p == "likes":
        comments = Comment.query.order_by(Comment.likes)[::-1]
    elif p == "dislikes":
        comments = Comment.query.order_by(Comment.dislikes)[::-1]
    for comment in comments:
        if comment.blog_id == id:
            commentsx.append(comment)
    if current_user.is_authenticated:
        if current_user.points >= 0:
            return render_template("baseblog.html", title=title, content=content, tags=tags, time=time, views=views, id=id, likes=likes, dislikes=dislikes, words=words, read_time=read_time, comments=commentsx, show=True, related=actrel[:10], bookmarked=bookmarked, note=note)
        else:
            return render_template("baseblog.html", title=title, content=content, tags=tags, time=time, views=views, id=id, likes=likes, dislikes=dislikes, words=words, read_time=read_time, comments=commentsx, show=False, login=False, msg="You need to have a positive number of points", related=actrel[:10], bookmarked=bookmarked, note=note)
    else:
        return render_template("baseblog.html", title=title, content=content, tags=tags, time=time, views=views, id=id, likes=likes, dislikes=dislikes, words=words, read_time=read_time, comments=commentsx, show=False, login=True, related=actrel[:10], bookmarked=bookmarked, note=note)

@blogs.route("/blogs/tags/<name>")
def see_tags_all(name):
    tag = db.session.query(Tag).filter(Tag.name == name).first()
    y = tag.name
    n = []
    uuu = []
    dict = {}
    extdict = {}
    views = 0
    words = 0
    blogs = db.session.query(Blog).all()
    for blog in blogs:
            id = blog.id
            hhh = blog.title
            yyy = get_single_blog(id)
            zzz = yyy["single_blog"]["tags"]
            lll = []
            for pp in range(len(zzz)):
                aaa = zzz[pp]["name"]
                if aaa == y:
                    views += blog.views
                    uuu.append(blog)
                    extdict[id] = yyy
                    n.append(hhh)
                    lll.append(aaa)
                    words += (len(blog.content.split()))
    
    posts = tag.posts
    uuu.extend(posts)
    
    dict[y] = n
    things = len(uuu)
    average = views/things
    time_to_read = (math.floor(words/200) + 1)
    avwords = words/things
    avtime = time_to_read/things
    id = tag.id
    if current_user.is_authenticated:
        id = tag.id
        following = current_user.following
        if tag in following:
            id = tag.id
            return render_template("tagblogs.html", blogs=uuu, things=things, views=views, average=average, words=words, time_to_read=time_to_read, avwords=avwords, avtime=avtime, id=id, showf=False, unfollowf=True)
        else:
            return render_template("tagblogs.html", blogs=uuu, things=things, views=views, average=average, words=words, time_to_read=time_to_read, avwords=avwords, avtime=avtime, id=id, showf=True, unfollowf=False)
    else:
        return render_template("tagblogs.html", blogs=uuu, things=things, views=views, average=average, words=words, time_to_read=time_to_read, avwords=avwords, avtime=avtime, id=id, showf=False, unfollowf=False)

@blogs.route("/blogs/viewall")
def see_all_blogs():
    p = request.args.get("sort_by", default="views")
    if p == "likes":        
        blogs = Blog.query.order_by(Blog.likes)[::-1]
    elif p == "dislikes":
        blogs =  Blog.query.order_by(Blog.dislikes)[::-1]
    elif p == "views":
        blogs =  Blog.query.order_by(Blog.views)[::-1]
    elif p =="oldest":
        blogs = Blog.query.order_by(Blog.created_at)
    elif p == "newest":
        blogs = Blog.query.order_by(Blog.created_at)[::-1]
    elif p == "id":
        blogs = Blog.query.order_by(Blog.id)
    l = []
    for blog in blogs:
        x = []
        id = blog.id
        y = get_single_blog(id)
        z = y["single_blog"]["tags"]
        for i in range(len(z)):
            a = z[i]["name"]
            x.append(a)
        
        l.append(x)
    
    return render_template("allblogs.html", blogs=zip(blogs, l))

@blogs.route("/blogs/viewadd", methods=["GET", "POST"])
def blog_view_add():
    if request.method == "POST":   
        title = request.form["title"].replace(" ", "-")
        content = markdown.markdown(request.form["content"])
        feature_image = "stuff"
        new_blog = Blog(title=title, content=content, feature_image=feature_image)
        tags = request.form["tags"].split(" ")
        users = []
        for tag in tags:
            present_tag=Tag.query.filter_by(name=tag).first()
            if(present_tag):
                present_tag.blogs_associated.append(new_blog)
                followers = present_tag.followers
                for follower in followers:
                    if follower.id not in users:
                        users.append(follower.id)
            else:
                new_tag=Tag(name=tag)
                new_tag.blogs_associated.append(new_blog)
                db.session.add(new_tag)
            
        text = f"""<p><a href='/blogs/views/{title}'>{title}</a> was created"""
        for user in users:
            notification = Notifications(user_id=user, text=text)
            db.session.add(notification)    
        
        db.session.add(new_blog)
        db.session.commit()

        return redirect(f"/blogs/views/{title}")
    else:
        return render_template("blogadd.html")    

@blogs.route("/blogs/addlike/<id>")
def add_like_to_blog(id):
    blog = db.session.query(Blog).filter(Blog.id == id).first()
    l = blog.title
    blog.likes += 1
    blog.views -= 1
    db.session.commit()
    return redirect(f"/blogs/views/{l}")

@blogs.route("/blogs/adddislike/<id>")
def add_dislike_to_blog(id):
    blog = db.session.query(Blog).filter(Blog.id == id).first()
    l = blog.title
    blog.dislikes += 1
    blog.views -= 1
    db.session.commit()
    return redirect(f"/blogs/views/{l}")

@blogs.route("/blogs/remlike/<id>")
def rem_like_to_a_blog(id):
    blog = db.session.query(Blog).filter(Blog.id == id).first()
    l = blog.title
    blog.likes -= 1
    blog.views -= 1
    db.session.commit()
    return redirect(f"/blogs/views/{l}")

@blogs.route("/blogs/remdislike/<id>")
def rem_dislike_to_a_blog(id):
    blog = db.session.query(Blog).filter(Blog.id == id).first()
    l = blog.title
    blog.dislikes -= 1
    blog.views -= 1
    db.session.commit()
    return redirect(f"/blogs/views/{l}")

@blogs.route("/blogs/viewedit", methods=["GET", "POST"])
def edit_blog_view():
    id = request.args.get('id')
    blog = db.session.query(Blog).filter(Blog.id == id).first_or_404()
    xtitle = blog.title
    views = blog.views
    xcontent = blog.content
    if request.method == "POST":
        ntitle = request.form["title"].replace(" ", "-")
        content = markdown.markdown(request.form["content"])
        blog.title = ntitle
        blog.content = content
        db.session.commit()
        return render_template("editblog.html", title=ntitle, content=content, id=id, views=views,message=f'<p>go to your updated blog at <a href="/blogs/views/{ntitle}">{ntitle}</a></p>')
    else:
        return render_template("editblog.html", title=xtitle, content=xcontent, id=id, views=views)

@login_required
@blogs.route("/blogs/create-comment/<int:id>", methods=["POST"])
def create_comment_on_blog(id):
    text = request.form["text"]
    author = request.form["author"]
    blog = db.session.query(Blog).filter(Blog.id == id).first()
    comment = Comment(text=text, author=author, blog_id=id, user_id=current_user.id)
    db.session.add(comment)
    db.session.commit()
    cid = getattr(comment, "id")
    return redirect(f"/blogs/views/{blog.title}#{cid}")

@login_required
@blogs.route("/blogs/create_reply/<int:id>", methods=["POST"])
def create_reply_on_blog(id):
    text = request.form["text"]
    author = request.form["author"]
    parent = request.args.get("parent")
    blog = db.session.query(Blog).filter(Blog.id == id).first()
    comment = Replies(text=text, author=author, blog_id=id, user_id=current_user.id, comment_id=parent)
    db.session.add(comment)
    db.session.commit()
    return redirect(f"/blogs/views/{blog.title}")

@blogs.route("/blogs/comments/addlike/<id>")
def addlike_to_coment(id):
    comment = db.session.query(Comment).filter(Comment.id == id).first()
    comment.likes += 1
    blogi = comment.blog_id
    blog = db.session.query(Blog).filter(Blog.id == blogi).first()
    l = blog.title
    blog.views -= 1
    useri = comment.user_id
    user = db.session.query(User).filter(User.id == useri).first()
    user.points += 1
    db.session.commit()
    return redirect(f"/blogs/views/{l}")

@blogs.route("/blogs/comments/adddislike/<id>")
def add_dislike_to_comment(id):
    comment = db.session.query(Comment).filter(Comment.id == id).first()
    comment.dislikes += 1
    blogi = comment.blog_id
    blog = db.session.query(Blog).filter(Blog.id == blogi).first()
    l = blog.title
    blog.views -= 1
    useri = comment.user_id
    user = db.session.query(User).filter(User.id == useri).first()
    user.points -= 1
    db.session.commit()
    return redirect(f"/blogs/views/{l}")

@login_required
@blogs.route("/blogs/comments/report/<id>")
def report_comment(id):
    comment = db.session.query(Comment).filter(Comment.id == id).first()
    comment.text = f"This comment has been reported by {current_user.name}"
    blogi = comment.blog_id
    blog = db.session.query(Blog).filter(Blog.id == blogi).first()
    l = blog.title
    blog.views -= 1
    db.session.commit()
    return redirect(f"/blogs/views/{l}")

@blogs.route("/blogs/replies/addlike/<id>")
def addlike_to_reply(id):
    comment = db.session.query(Replies).filter(Replies.id == id).first()
    comment.likes += 1
    blogi = comment.blog_id
    blog = db.session.query(Blog).filter(Blog.id == blogi).first()
    l = blog.title
    blog.views -= 1
    db.session.commit()
    return redirect(f"/blogs/views/{l}")

@login_required
@blogs.route("/test/bookmarks")
def test_user_bookmarks():
    bookmarks = current_user.bookmarks
    return f"bookmarks: {bookmarks}"

@blogs.route("/blog/bookmarks")
def see_all_bookmarks():
    bookmarks = db.session.query(Bookmark).all()
    return f"bookmarks: {bookmarks}"

@blogs.route("/blogs/make-newsletter/<int:id>")
def make_blog_a_newsletter(id):
    blog = Blog.query.filter_by(id=id).first()
    title = Blog.title
    content = f"""
    <html>
    <body style="background-color: black; color: white">
    <div style="border-radius: 25px;">
    {blog.content}
    </div>
    <p>{blog.likes} likes | {blog.dislikes} dislikes</p>
    <p>{len(blog.comments)} comments</p>
    """
    users = User.query.filter_by(newsletter=True).all()
    if users:
        x = []
        for user in users:
            x.append(user.email)
        
        h = send_newsletter_with_flask(title=title, addresses=x, content=content)
        
        if h == "sent":
            return "sent"
        else:
            return "error"
    else:
        return "not anyone to send to!"


@blogs.route("/blog/addbookmark/<id>", methods=["POST", "GET"])
def addbookmark_to_blog(id):
    if request.method == "POST":
        blog = db.session.query(Blog).filter(Blog.id == id).first()
        note = request.form.get("note")
        cid = request.args.get("user_id")
        new = Bookmark(blog_id=blog.id, user_id=cid, note=note)
        db.session.add(new)
        db.session.commit()
        return redirect("/dashboard")


@blogs.route("/blog/deletebookmark/<id>")
def delete_bookmark(id):
    bookmark = db.session.query(Bookmark).filter(Bookmark.id == id).first()
    db.session.delete(bookmark)
    db.session.commit()

@blogs.route("/blog/bookmark/edit/<id>", methods=["POST"])
def edit_bookmark(id):
    bookmark = Bookmark.query.filter_by(blog_id=id).first()
    note = request.form.get("note")
    bookmark.note = note
    db.session.commit()
    return redirect(f"/blog/view/{id}")
    
@blogs.route("/blogs/find/related/<id>")
def related_tags_thingy(id):
    t = Tag.query.filter_by(id=id).first()
    name = t.name
    dictx = {}
    blogs = Blog.query.order_by(Blog.views)
    for blog in blogs:
        tags = blog.tags
        if t in tags:
            for tag in tags:
                if tag.name in dictx:
                    dictx[tag.name] += 1
                elif tag.name != name:
                    dictx[tag.name] = 1
    
    posts = Post.query.order_by(Post.views)
    for post in posts:
        tagsp = post.tags
        if t in tagsp:
            for tagx in tagsp:
                if tagx.name in dictx:
                    dictx[tagx.name] += 1
                elif tagx.name != name:
                    dictx[tagx.name] = 1
    
    return dict(sorted(dictx.items(), key=lambda item: item[1], reverse=True))

@blogs.route("/api/blog/bookmark/add", methods=["POST"])
def add_api_bookmark_things():
    data = request.get_json()
    user_id = data["user_id"]
    blog_id = data["blog_id"]
    note = data["note"]
    new = Bookmark(user_id=user_id, blog_id=blog_id, note=note)
    db.session.add(new)
    db.session.commit()
    bookmark_id = getattr(new, "id")
    return {"id": bookmark_id}

# app.register_blueprint(blogs, url_prefix="/")