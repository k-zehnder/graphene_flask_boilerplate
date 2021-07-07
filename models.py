from peewee import *
import pandas as pd
import numpy as np
import phonenumbers
from phonenumbers import geocoder
from phonenumbers.timezone import time_zones_for_number
from faker import Faker
import datetime
import pytz
import os

# initialize db
db = SqliteDatabase('respondNoTwilio.db')

# Base model for work with Database through ORM
class BaseModel(Model):
    class Meta:
        database = db  # connection with database

# Modules
# db = SQLAlchemy(app)

# Models
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    books = db.relationship('Book', backref='author')

    def __init__(self, username, email):
      self.username = username
      self.email = email

    def __repr__(self):
        return '<User %r>' % self.id

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Book %r>' % self.title % self.description % self.year % self.author_id
