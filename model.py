"""Model for project 2"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_email = db.Column(db.String, unique=True, nullable=False)
    user_password = db.Column(db.String(15), nullable=False)
    user_firstname = db.Column(db.String(15), nullable=False)
    user_lastname = db.Column(db.String(15), nullable=False)
    user_favoritegenre = db.Column(db.String(15), nullable=False)
    user_location = db.Column(db.String(15), nullable=False)
    user_books = db.Column(db.String)

class Book(db.Model):
    """Book"""

    __tablename__ = "books"

    book_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_title = db.Column(db.String, nullable=False, unique=True)
    book_genre = db.Column(db.String, nullable=False)
    book_author = db.Column(db.String, nullable=False)