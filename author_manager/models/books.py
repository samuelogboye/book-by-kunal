#!/usr/bin/env python3
"""Template for the User Class"""

from author_manager import db
from author_manager.models.base import BaseModel

class Book(BaseModel):
        """ Books class"""
        __tablename__ = 'books'

        title = db.Column(db.String(100), nullable=False)
        year = db.Column(db.Integer, nullable=False)
        author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

        def __init__(self, title, year, author_id):
            super().__init__()
            self.title = title
            self.year = year
            self.author_id = author_id

        def __repr__(self):
            """Return a representation of the object"""
            return f"<Book {self.title}>"

        def format(self):
            """Format the object's attributes as a dictionary"""
            return {
                'id': self.id,
                'title': self.title,
                'year': self.year,
                'author_id': self.author_id
            }