from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path 
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "workout.db"

# UPLOAD_FOLDER = path.join(path.dirname(path.abspath(__file__)), 'uploads')
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def initialize():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "bUWp8Fugqgn67ZfmAPDv6nd1lqQIsXBX"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .structure import structure
    from .calculators import calculators
    from .blogs import blogs
    from .form import form

    app.register_blueprint(structure, url_prefix="/")
    app.register_blueprint(calculators, url_prefix="/")
    app.register_blueprint(blogs, url_prefix="/")
    app.register_blueprint(form, url_prefix="/")

    from .model import Workout, User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'form.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
    print("created Database!")