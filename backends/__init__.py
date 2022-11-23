from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin
from flask_mail import Mail, Message
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_socketio import SocketIO, send
from flask_migrate import Migrate
from os import path


DB_NAME = "database.db"
db = SQLAlchemy()
mail = Mail()
socketio = SocketIO()
migrate = Migrate()

def create_app():
    apibp = Blueprint("api", __name__)
    api = Api(apibp)

    app = Flask(__name__)
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
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
    mail.init_app(app)
    db.init_app(app)
    CORS(app, resources={r"*": {"origins": "*"}})
    socketio.init_app(app, cors_allowed_origins="*")
    
    from .auth import auth
    from .home import home
    from .todo import todo
    from .newsletter import newsletter
    from .book import book
    from .help import help
    from .blogs import blogs
    from .user import user
    from .community import community
    from .chat import chat
    from .search import search
    from .card import card
    from .quiz import quiz
    from .upload import upload
    from .cars import cars
    from .airplanes import airplanes
    from .restauraunts import restauraunts
    from .songs import songs
    from .bank import bank
    from .ide import ide
    from .c import c
    from .notes import notes
    from backends.url_shortener.add import add_url
    from backends.url_shortener.view import view_url
    # from .stream import stream
    from .svelte import svelte
    from .go import go
    from .shop import shop
    from backends.cli.clix import clix
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(todo, url_prefix='/')
    app.register_blueprint(newsletter, url_prefix="/")
    app.register_blueprint(book, url_prefix="/")
    app.register_blueprint(help, url_prefix="/")
    app.register_blueprint(blogs, url_prefix="/")
    app.register_blueprint(user, url_prefix="/")
    app.register_blueprint(community, url_prefix="/")
    app.register_blueprint(chat, url_prefix="/")
    app.register_blueprint(search, url_prefix="/")
    app.register_blueprint(card, url_prefix="/")
    app.register_blueprint(quiz, url_prefix="/")
    app.register_blueprint(upload, url_prefix="/")
    app.register_blueprint(cars, url_prefix="/")
    app.register_blueprint(airplanes, url_prefix="/")
    app.register_blueprint(restauraunts, url_prefix="/")
    app.register_blueprint(songs, url_prefix="/")
    app.register_blueprint(bank, url_prefix="/")
    app.register_blueprint(svelte, url_prefix="/")
    app.register_blueprint(ide, url_prefix="/")
    app.register_blueprint(c, url_prefix="/")
    app.register_blueprint(notes, url_prefix="/")
    app.register_blueprint(go, url_prefix="/")
    app.register_blueprint(shop, url_prefix="/")
    app.register_blueprint(clix, url_prfix="/")
    app.register_blueprint(apibp, url_prfix="/")
    app.register_blueprint(add_url, url_prefix="/")
    app.register_blueprint(view_url, url_prfix="/")
    # app.register_blueprint(stream, url_prefix="/")
    
    api.init_app(app)
    from .apix import Randomz, top_bbc_news, HelloWorld, ftse100, GBPTOEUR, Banana, APIrickroll
    
    api.add_resource(Randomz, '/api/random', endpoint="get_random_thingy")
    api.add_resource(top_bbc_news, "/api/news/bbc/top")
    api.add_resource(HelloWorld, '/api/test')
    api.add_resource(GBPTOEUR, '/api/convert/EURTOGBP')
    api.add_resource(ftse100, '/api/ecenomics/ftse100')
    api.add_resource(APIrickroll, '/api/test/dQw4w9WgXcQ')
    api.add_resource(Banana, '/api/test/food')
    
    
    from .models import User
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @app.errorhandler(500)
    def internal_server_error(e):
        return f"Something went wrong : {e}", 500

    @app.errorhandler(405)
    def method_not_allowed(e):

        if request.path.startswith('/api/'):
            
            return jsonify(message="Method Not Allowed"), 405
        else:
            return "wrong method!" , 405

    @app.errorhandler(404)
    def page_not_found(e):
        return f"<h1>404!</h1><p>We couldn't find the requested route on the website</p><p>Sorry could not find this, please try again!!</p>"

    @app.after_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

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
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
    
    
    db.create_all(app=app)

    return app
