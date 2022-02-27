import bcrypt
from flask_login import UserMixin
from WarwickHackAThon2 import db

class user(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    emailAddress = db.column(db.String(50))
    password = db.column(db.String(50))