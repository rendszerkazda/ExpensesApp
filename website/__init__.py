from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'adfgsvfgv'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import  auth
    
    app.register_blueprint(views, url_prefix="/") # prefix the url with /
    app.register_blueprint(auth, url_prefix="/") # prefix the url with /auth
    
    from .models import User, Expenses
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # redirect to login page if not logged in
    login_manager.init_app(app) # initialize login manager
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # get user by id from database
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Database!")