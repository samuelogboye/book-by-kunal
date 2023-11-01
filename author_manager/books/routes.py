from flask import Blueprint, jsonify, request
from author_manager import db
from uuid import UUID
from typing import Dict, List
from datetime import datetime
from author_manager.books.book_schema import IdSchema


books = Blueprint("books", __name__, url_prefix="/api/books")

@books.route("/", methods=["GET"])
def test():
        return jsonify({"model": "book", "message": "Hello World!", "status": "OK"})