from flask_login import UserMixin
from sqlalchemy import or_
from datetime import datetime
from . import db
from backends.utilities.discord import discord_notifier
from backends.supplementary.aes import AESCipher
import html

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

class Emaillist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emailadd = db.Column(db.String(1000), unique=True)


class Readinglist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list = db.Column(db.String(1000))
    author = db.Column(db.String(1000))
    summary = db.Column(db.String(1000))
    pages = db.Column(db.Integer)
    rating = db.Column(db.Float)

    
class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    brand = db.Column(db.String(150))
    top_speed = db.Column(db.Float)
    horsepower = db.Column(db.Integer)
    length = db.Column(db.Float)
    width = db.Column(db.Float)
    rating = db.Column(db.Float, default=4.5)

class bank_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    money = db.Column(db.Float)
    account_type = db.Column(db.String(100))

    
class airplane(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(200))
    length = db.Column(db.Float)
    width = db.Column(db.Float)
    # altitude = db.Column(db.Integer)
    top_speed = db.Column(db.Integer)
    airline = db.Column(db.String(200))
    base = db.Column(db.String(200))


class boat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    top_speed = db.Column(db.Integer)
    length = db.Column(db.Float)

class restauraunt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    overall_rating = db.Column(db.Float)
   
    
chat_user = db.Table("chat_user", 
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("chat_id", db.Integer, db.ForeignKey("chat.id"))
)

class Snake_leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    score = db.Column(db.Integer)
    food = db.Column(db.Integer)
    name = db.Column(db.String(200))

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255))
    texts = db.relationship("Text", backref="chat")
    users = db.relationship("User", secondary=chat_user, backref=db.backref("chats", lazy="dynamic"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(2000))
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
    authorname = db.Column(db.String(150))
    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"))
    reactions = db.relationship("Reaction", backref="text")

class Reaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(1))
    author = db.Column(db.String(150))
    text_id = db.Column(db.Integer, db.ForeignKey("text.id"))

class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150))
    read = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def send_discord(self):
        user_id = self.user_id
        user = User.query.filter_by(id=user_id).first()
        if user.discord_webhook:
            decryptor = AESCipher("discord webhook")
            discord_webhook = decryptor.decrypt(user.discord_webhook)
            new = discord_notifier(url=discord_webhook)
            new.add_embed(description=self.text, title="New notification")
            new.send()
    
    def add(self, text, user_id):
        new = Notifications(text=text, user_id=user_id)
        db.session.add(new)
        db.session.commit()
        self.send_discord()


user_tag = db.Table("user_tag", 
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'), primary_key=True), 
    db.Column('user_id',db.Integer,db.ForeignKey('user.id'), primary_key=True)
)

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id')),
    # db.Column('timestamp'), db.DateTime, default=datetime.utcnow
)

user_category = db.Table("user_category",
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(50))
    points = db.Column(db.Integer, default=1)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
    comments = db.relationship('Comment', backref="user")
    security_key = db.Column(db.String(65))
    validated = db.Column(db.Boolean(), default=False)
    newsletter = db.Column(db.Boolean(), default=False)
    description = db.Column(db.Text, nullable=True, default="N/A")
    notifications = db.relationship('Notifications', backref="user")
    snake = db.relationship("Snake_leaderboard", backref="user")
    bookmarks = db.relationship('Bookmark', backref="user")
    super_user = db.Column(db.Boolean(), default=False)
    mod = db.Column(db.Boolean(), default=False)
    posts = db.relationship('Post', backref="user")
    awnsers = db.relationship('Awnser', backref="user")
    following = db.relationship("Tag", secondary=user_tag, backref=db.backref("followers", lazy="dynamic"))
    quizzes = db.relationship("Quiz", backref="user")
    notes = db.relationship("Note", backref="user")
    objects = db.relationship("Object", backref="user")
    items = db.relationship("Item", backref="user")
    checkouts = db.relationship("Checkout", backref="user")
    shopaccount = db.relationship("Shopaccount", backref="user")
    urls = db.relationship("Urlshortner", backref="user")
    reviews = db.relationship("Review", backref="user")
    webviews = db.relationship("WebView", backref="user")
    # discord_wbhook = db.Column(db.Text)
    guides = db.relationship("Guide", backref="user")
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    
    def older_than(self, date):
        time = datetime.utcnow
        created_at = self.timestamp
        date = time.replace(day=time.day - date)
        if date > created_at:
            return True
        return False
    
    def delete(self):
        posts = self.posts
        guides = self.guides
        urls = self.urls
        notes = self.notes
        for url in urls:
            db.session.delete(url)
        

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0
    
    def followed_posts(self):
        return Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id).order_by(
                    Post.views.desc())
    
    def current_checkout(self):
        checkouts = self.checkouts
        list = []
        for check in checkouts:
            if not check.sold:
                list.append(check)
        
        return list[0]


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"), nullable=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Tag(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    
    @property
    def serialize(self):
        return {
        'id': self.id,
        'name': self.name     
        }


# class follow(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#     following = db.relationship("Tag", secondary=user_tag, backref=db.backref("followers", lazy="dynamic"))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    author = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    replies = db.relationship(
        'Replies', backref="replies")

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    note = db.Column(db.String(200), nullable=True)

class Replies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    author = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    comment_id = db.Column(db.Integer, db.ForeignKey("comment.id"))

tag_blog = db.Table('tag_blog',
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'), primary_key=True),
    db.Column('blog_id', db.Integer,db.ForeignKey('blog.id'),primary_key=True)
)

tag_post = db.Table('tag_post',
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'), primary_key=True),
    db.Column('post_id', db.Integer,db.ForeignKey('post.id'),primary_key=True)
)

tag_guide = db.Table('tag_guide',
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'), primary_key=True),
    db.Column('guide_id', db.Integer,db.ForeignKey('guide.id'),primary_key=True)
)

tag_help = db.Table('tag_help',
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'), primary_key=True),
    db.Column('help_id', db.Integer,db.ForeignKey('help.id'),primary_key=True)
)


class Blog(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    content=db.Column(db.Text,nullable=False)
    feature_image= db.Column(db.String,nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    views = db.Column(db.Integer, default=0)
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    tags=db.relationship('Tag',secondary=tag_blog,backref=db.backref('blogs_associated',lazy="dynamic"))
    comments = db.relationship('Comment', backref="blog")
    bookmarks = db.relationship('Bookmark', backref="blog")

    def make_help(self):
        question = self.title
        awnser = self.content
        awnser = html.unescape(awnser)
        tags = self.tags
        if len(tags) < 1:
            return False
        subject = tags[0].name
        new = Help(subject=subject, awnser=awnser, question=question)
        db.session.add(new)
        db.session.commit()
        id = getattr(new, "id")
        for tag in tags:
            tag.help.append(new)
        db.session.commit()

        return id
 
    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'feature_image': self.feature_image,
            'created_at': self.created_at,
            'views': self.views,
            'likes': self.likes,
            'dislikes': self.dislikes,
        }  

class Awnser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    best = db.Column(db.Boolean(), default=False)
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    author = db.Column(db.String(200))
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.Text)
    tags = db.relationship('Tag',secondary=tag_post,backref=db.backref('posts',lazy="dynamic"))
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    awnsers = db.relationship("Awnser", backref="post")
    views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship("Postcomment", backref="Post")

    def make_help(self):
        question = self.title
        awnser = self.content
        awnser = html.unescape(awnser)
        tags = self.tags
        if len(tags) < 1:
            return False
        subject = tags[0].name
        new = Help(subject=subject, awnser=awnser, question=question)
        db.session.add(new)
        db.session.commit()
        id = getattr(new, "id")
        for tag in tags:
            tag.help.append(new)
        db.session.commit()

        return id

    def remove_tag(self, name):
        tags = self.tags
        for tag in tags:
            if tag.name == name:
                self.tags.remove(tag)

class Postcomment(db.Model):
    _N = 6
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    author = db.Column(db.String(320))
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    parent_id = db.Column(db.Integer, db.ForeignKey("postcomment.id"), nullable=True)
    replies = db.relationship("Postcomment", backref=db.backref('parent', remote_side=[id]), lazy=True)
    path = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()
        parent = Postcomment.query.filter_by(id=self.parent_id).first()
        if parent:
            prefix = str(parent.path)
        else:
            prefix = ""
        self.path = prefix + '{:0{}d}'.format(self.id, self._N)
        db.session.commit()
    
    def level(self):
        return self.path


class Qawnser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    awnser = db.Column(db.Text)
    correct = db.Column(db.Boolean)
    error = db.Column(db.Integer, nullable=True, default=None)

class Singlequestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    awnser = db.Column(db.Text)
    question = db.Column(db.Text)
    type = db.Column(db.String(400))
    error = db.Column(db.Integer)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quiz.id"))

class Multiplechoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    awnsers = db.relationship("Multiawnser", backref="question")
    quiz_id = db.Column(db.Integer, db.ForeignKey("quiz.id"))

class Multiawnser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    awnser = db.Column(db.Text)
    correct = db.Column(db.Boolean)
    question_id = db.Column(db.Integer, db.ForeignKey("multiplechoice.id"))

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    awnser = db.relationship("Qawnser", backref="question")
    hint = db.Column(db.String(200))
    quiz_id = db.Column(db.Integer, db.ForeignKey("quiz.id"))

quiz_category = db.Table("quiz_category",
   db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True),
   db.Column('quiz_id', db.Integer, db.ForeignKey('quiz.id'), primary_key=True)
)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.String(200), nullable=True)
    name = db.Column(db.String(200))
    questions = db.relationship("Question", backref="quiz")
    multiple_choice = db.relationship("Multiplechoice", backref="quiz")
    single_choice = db.relationship("Singlequestion", backref="quiz")
    category = db.relationship('Category',secondary=quiz_category,backref=db.backref('quiz',lazy="dynamic"))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))

card_category = db.Table("card_category",
    db.Column("card_id", db.Integer, db.ForeignKey('card.id')),
    db.Column("stacktype_id", db.Integer, db.ForeignKey('stacktype.id'))
)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(500))
    back = db.Column(db.Text)
    correct = db.Column(db.Boolean(), default=False)
    stack_id = db.Column(db.Integer, db.ForeignKey("stack.id"))

class Stacktype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

class Stack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.Text)
    cards = db.relationship("Card", backref="stack")


class Help(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(1000))
    question = db.Column(db.String(1000))
    awnser = db.Column(db.String(1000))
    tags=db.relationship('Tag',secondary=tag_help,backref=db.backref('help',lazy="dynamic"))
    # FUTURE ME: REMEBER TO MAKE THIS SO THAT WHEN SOMEONE SEARCHES FOR HELP ON SOMETHING THEY GET CORRECT AWNSER BACK, IE: ?topic:chemistry&q="electron" GOES TO {"electron": "A subatomic particle with a negative charge and orbits the nuclues in shells"}

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"), nullable=True, default=None)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=True, default=None)
    stack_id = db.Column(db.Integer, db.ForeignKey("stack.id"), nullable=True, default=None)

    def part_of_blog(self, id):
        if self.blog_id == id:
            return True
        else:
            return False

    
    def part_of_post(self, id):
        if self.post_id == id:
            return True
        else:
            return False
    
    def part_of_stack(self, id):
        if self.stack_id == id:
            return True
        else:
            return False


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    lyrics = db.Column(db.Text)

itme_tags = db.Table("item_tags",
    db.Column("item_id",db.Integer, db.ForeignKey("item.id")))

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.Integer)
    description = db.Column(db.Text)
    title = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    objects = db.relationship("Object", backref="item")
    price = db.Column(db.String(10))
    reviews = db.relationship("Review", backref="item")
    def create(self, stock: int):
        for i in range(stock):
            new = Object(item_id=self.id, price=self.price)
            db.session.add(new)
        db.session.commit()

    def userbought(self, user):
        items = self.objects
        for itm in items:
            user_id = itm.user_id
            if user_id == user or user_id == self.user_id:
                return True
        else:
            return False
    
    def average_review(self):
        reviews = self.reviews
        stars = 0
        for rev in reviews:
            star = rev.stars
            stars += star
        if len(reviews) > 0:
            return stars/len(reviews)
        else:
            return "no reviews"
    
    def free_objects(self):
        objects = self.objects
        list = []
        for obj in objects:
            if not obj.sold:
                list.append(obj)
        
        return list
    
    def checkouts(self):
        dict = {}
        checkouts = Checkout.query.all()
        for check in checkouts:
            items = check.show_items()
            if self.id in items:
                for itm in items:
                    item = Item.query.filter_by(id=itm).first()
                    if item.title in dict:
                        dict[item.title] += 1
                    elif item.title != self.title:
                        dict[item.title] = 1

        return dict
    

class Checkout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    objects = db.relationship("Object", backref="checkout")
    sold = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def sell(self):
        for obj in self.objects:
            obj.sold = True
            obj.user_id = self.user_id
        self.sold = True
        db.session.commit()
    
    def show_items(self):
        dict = {}
        objects = self.objects
        for obj in objects:
            item_id = obj.item_id
            if item_id in dict:
                dict[item_id].append(obj.id)
            else:
                dict[item_id] = [obj.id]
        
        return dict
    
    def current_checkout(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        checkouts = user.checkouts
        list = []
        for check in checkouts:
            if not check.sold:
                list.append(check)
        
        return list[0]


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    sold = db.Column(db.Boolean(), default=False)
    price = db.Column(db.String(5))
    checkout_id = db.Column(db.Integer, db.ForeignKey("checkout.id"), nullable=True, default=None)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True, default=None)
    added_to_checkout = db.Column(db.DateTime, nullable=True, default=None)

    def seller(self):
        item = Item.query.filter_by(id=self.item_id).first()
        if item:
            return item.user_id
    
    def item_name(self):
        item = Item.query.filter_by(id=self.item_id).first()
        if item:
            return item.title

class Urlshortner(db.Model):
    id = db.Column(db.String, primary_key=True)
    actual = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class ImageCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer, db.ForeignKey("card.id"))
    filename = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Shopaccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    credit_card = db.Column(db.Text)
    telephone = db.Column(db.Text, nullable=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Float)
    text = db.Column(db.Text)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Newssource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    url = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    pattern = db.Column(db.Text, nullable=True)
    tag = db.Column(db.Text, nullable=True)
    headlines = db.relationship("Headline", backref="news")
    rss = db.Column(db.Boolean(), default=False)

class Headline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    news_id = db.Column(db.Integer, db.ForeignKey("newssource.id"))

calendar_event = db.Table("calendar_event",
    db.Column("event_id", db.Integer, primary_key=True),
    db.Column("calendar_id", db.Integer, primary_key=True)
)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_scheduled = db.Column(db.DateTime)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    users = db.relationship("User", backref="event")
    calendar_id = db.Column(db.Integer, db.ForeignKey("calendar.id"))

class Calendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    events = db.relationship("Event", backref="calendar")

class ScamPhone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telephone_code = db.Column(db.Text)
    area_code = db.Column(db.Text)

class ScamEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text)

class SocialPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    content = db.Column(db.Text)

class ImageGuide(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    guide_id = db.Column(db.Integer, db.ForeignKey("guide.id"))
    name = db.Column(db.Text)

class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    images = db.relationship("ImageGuide")
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tags=db.relationship('Tag',secondary=tag_guide,backref=db.backref('guides',lazy="dynamic"))
    likes = db.relationship("GuideLike")
    likes = db.relationship("GuideDisLike")

class GuideLike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guide_id = db.Column(db.Integer, db.ForeignKey("guide.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class GuideDisLike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guide_id = db.Column(db.Integer, db.ForeignKey("guide.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class WebView(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    def post_views(self, title):
        views = WebView.query.all()
        out = []
        for view in views:
            if f"/community/{title}" in views:
                out.append(view)

        return out
    
    def guide_views(self):
        pass
