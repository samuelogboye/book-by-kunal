from flask import Blueprint, jsonify, request
from author_manager import db
from uuid import UUID
from typing import Dict, List
from datetime import datetime
from author_manager.models.authors import Author
from author_manager.authors.author_schema import IdSchema


authors = Blueprint("authors", __name__, url_prefix="/api/authors")

@authors.route("/tests", methods=["GET"])
def test():
        return jsonify({"model": "authors", "message": "Hello World!", "status": "OK"})


@authors.route("/", methods=["POST"])
def create_author():
    """Create a new author"""
    # Get the request body
    body: Dict = request.get_json()
    # Check that all required fields are present
    if not all(
        key in body.keys()
        for key in ("first_name", "last_name")
    ):
        return jsonify({"message": "Invalid request body", "status": "error"}), 400

    if Author.query.filter_by(first_name=body["first_name"], last_name=body["last_name"]).first():
        return jsonify({"message": "Author already exists", "status": "error"}), 400

    # Create a new author instance
    author = Author(
        first_name=body["first_name"],
        last_name=body["last_name"]
    )
    # Save the new author
    author.insert()
    # Return a response with a new author's details
    return jsonify({"author": author.format(), "status": "success"}), 201


@authors.route("/", methods=["GET"])
def get_authors():
    """Get all authors"""
    # Get all authors from the database
    authors = Author.query.all()
    # Return a response with a list of authors
    return jsonify({"authors": [author.format() for author in authors], "status": "success"}), 200


@authors.route("/<author_id>", methods=["GET"])
def get_author(author_id : UUID) -> dict:
    """Get a single author"""
    # Validate the author's id
    author_id = IdSchema(id=author_id).id

    # Get the author from the database
    author = Author.query.filter_by(id=author_id).first()
    # Check if the author exists
    if not author:
        return jsonify({"message": "Author not found", "status": "error"}), 404
    # Return a response with an author's details
    return jsonify({"author": author.format(), "status": "success"}), 200


@authors.route("/<author_id>", methods=["PUT"])
def update_author(author_id : UUID) -> dict:
    """Update an author"""
    # Validate the author's id
    author_id = IdSchema(id=author_id).id

    # Get the request body
    body: Dict = request.get_json()
    # Check that all required fields are present
    if not all(
        key in body.keys()
        for key in ("first_name", "last_name")
    ):
        return jsonify({"message": "Invalid request body", "status": "error"}), 400

    # Get the author from the database
    author = Author.query.filter_by(id=author_id).first()
    # Check if the author exists
    if not author:
        return jsonify({"message": "Author not found", "status": "error"}), 404

    # Update the author's details
    author.first_name = body["first_name"]
    author.last_name = body["last_name"]
    # Save the changes
    author.update()
    # Return a response with an author's details
    return jsonify({"author": author.format(), "status": "success"}), 200