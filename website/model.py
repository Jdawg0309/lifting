from . import db
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))
    firstName = db.Column(db.String(30))
    lastName = db.Column(db.String(30))
    workout_data = db.relationship('Workout')
    physique_data = db.relationship('Physique')

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    rpe = db.Column(db.Float, nullable=False)
    username = db.Column(db.String(30), db.ForeignKey('user.username'), nullable=False)

class Physique(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    weight = db.Column(db.Float, nullable=True)
    comments = db.Column(db.String(100000), nullable=True)
    img = db.Column(db.Text, nullable=False)
    imgName = db.Column(db.Text, nullable=False)
    mimeType = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(30), db.ForeignKey('user.username'))