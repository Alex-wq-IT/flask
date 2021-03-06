from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    security = db.Column(db.Integer)
