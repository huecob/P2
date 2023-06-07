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

    messages_received = db.relationship("DirectMessages", back_populates="sent_message")
    messages_sent = db.relationship("DirectMessages", back_populates="got_message")

class Book(db.Model):
    """Book"""

    __tablename__ = "books"

    book_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_title = db.Column(db.String, nullable=False, unique=True)
    book_genre = db.Column(db.String, nullable=False)
    book_author = db.Column(db.String, nullable=False)
    book_comments = db.Column(db.String) #foreign key from comments/messages

class Genre(db.Model):
    """Book Genres"""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    genre_name = db.Column(db.String, unique=True, nullable=False)

class DirectMessages(db.Model):
    """Log of all messages"""

    __tablename__ = "messages"

    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    message_contents = db.Column(db.String)

    sent_message = db.relationship("User", back_populates="message_sent")
    
