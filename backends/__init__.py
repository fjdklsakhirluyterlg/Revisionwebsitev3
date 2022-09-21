from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin
from flask_mail import Mail, Message
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_socketio import SocketIO, send
from os import path

DB_NAME = "database.db"
db = SQLAlchemy()
api = Api()
mail = Mail()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    CORS(app, resources={r"*": {"origins": "*"}})
    
    # from .auth import auth
    from .home import home
    # from .todo import todo
    # from .newsletter import newsletter
    # from .book import book
    # from .help import help
    # from .blogs import blogs
    # from .user import user
    # from .community import community
    # from .chat import chat
    # from .search import search
    # from .card import card
    # from .quiz import quiz
    # from .upload import upload
    # from .cars import cars
    # from .airplanes import airplanes
    # from .restauraunts import restauraunts
    # from .songs import songs
    # from .bank import bank
    # # app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(home, url_prefix='/')
    # app.register_blueprint(todo, url_prefix='/')
    # app.register_blueprint(newsletter, url_prefix="/")
    # app.register_blueprint(book, url_prefix="/")
    # app.register_blueprint(help, url_prefix="/")
    # app.register_blueprint(blogs, url_prefix="/")
    # app.register_blueprint(user, url_prefix="/")
    # app.register_blueprint(community, url_prefix="/")
    # app.register_blueprint(chat, url_prefix="/")
    # app.register_blueprint(search, url_prefix="/")
    # app.register_blueprint(card, url_prefix="/")
    # app.register_blueprint(quiz, url_prefix="/")
    # app.register_blueprint(upload, url_prefix="/")
    # app.register_blueprint(cars, url_prefix="/")
    # app.register_blueprint(airplanes, url_prefix="/")
    # app.register_blueprint(restauraunts, url_prefix="/")
    # app.register_blueprint(songs, url_prefix="/")
    # app.register_blueprint(bank, url_prefix="/")
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))

    @app.errorhandler(500)
    def internal_server_error(e):
        return f"Something went wrong : {e}", 500

    @app.errorhandler(405)
    def method_not_allowed(e):

        if request.path.startswith('/api/'):
            
            return jsonify(message="Method Not Allowed"), 405
        else:
            return "wrong method!"

    @app.errorhandler(404)
    def page_not_found(e):
        return f"Sorry could not find this"

    app.register_error_handler(404, page_not_found)

    app.config['SQLALCHEMY_DATABASE_URI'] =f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "key"
    app.config['MAIL_SERVER']='smtp.outlook.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'drive1.banerjee.armaan@outlook.com'
    app.config['MAIL_PASSWORD'] = 'Transport11.'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
    
    
    db.create_all(app=app)
    print('Created Database!')
    
    
    return app


app = create_app()