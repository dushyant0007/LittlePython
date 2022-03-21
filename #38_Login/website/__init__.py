import imp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy, Model
from os import path
from flask_login import login_manager, LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "hello"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'
    db.init_app(app)
    login_manager  = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)



    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # db.create_all(app=app)

    return app
