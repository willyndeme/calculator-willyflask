import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()

db=SQLAlchemy()
bcrypt=Bcrypt()
login=LoginManager()

def create_app():
    app=Flask(__name__)

    app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)
    bcrypt.init_app(app)
    login.init_app(app)
    login.login_view='use.login'


    from calculator.User.routes import use
    from calculator.math.routes import math

    app.register_blueprint(use)
    app.register_blueprint(math)
        
    return app
