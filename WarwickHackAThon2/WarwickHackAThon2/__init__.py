"""
The flask application package.
"""
import os
from flask import Flask,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
from werkzeug.utils import secure_filename

#db = SQLAlchemy()

app = Flask(__name__)
#app.config['SECRET_KEY'] = '625273'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

#db.init_app(app)

#login_manager = LoginManager()
#login_manager.login_view = "views.login"
#login_manager.init_app(app)
import WarwickHackAThon2.views
