#!/usr/bin/env python3
"""Template for the User Class"""

from author_manager import db
from author_manager.models.base import BaseModel
from author_manager.models.books import Book

class Author(BaseModel):
        """ Authors class"""
        __tablename__ = 'authors'

        first_name = db.Column(db.String(100), nullable=False)
        last_name = db.Column(db.String(100), nullable=False)
        books = db.relationship('Book', backref='author', lazy=True, cascade="all, delete-orphan")

        def __init__(self, first_name, last_name):
            super().__init__()
            self.first_name = first_name
            self.last_name = last_name

        def __repr__(self):
            """Return a representation of the object"""
            return f"<Author {self.first_name} {self.last_name}>"

        def format(self):
                """Format the object's attributes as a dictionary"""
                return {
                        'id': self.id,
                        'first_name': self.first_name,
                        'last_name': self.last_name,
                        'createdAt': self.createdAt,
                        'updatedAt': self.updatedAt,
                        'books': [book.format() for book in self.books]
                }