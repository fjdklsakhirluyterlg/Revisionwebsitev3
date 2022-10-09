from flask_login import UserMixin
from sqlalchemy import or_
from datetime import datetime
from . import db
from flask_sqlalchemy import SQLAlchemy

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

user_tag = db.Table("user_tag", 
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'), primary_key=True), 
    db.Column('user_id',db.Integer,db.ForeignKey('user.id'), primary_key=True)
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
    description = db.Column(db.String(500), nullable=True, default="N/A")
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

class Tag(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    # 
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


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(500))
    back = db.Column(db.Text)
    correct = db.Column(db.Boolean(), default=False)
    stack_id = db.Column(db.Integer, db.ForeignKey("stack.id"))

class Stack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String(250))
    cards = db.relationship("Card", backref="stack")

class Help(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(1000))
    topic = db.Column(db.String(1000))
    question = db.Column(db.String(1000))
    awnser = db.Column(db.String(1000))
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
