from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask
from author_manager.config import App_Config
from flask_caching import Cache


db = SQLAlchemy()


#Create an instance of the cach
cache = Cache()


def create_app():
    """
    Create a new instance of the app with the given configuration.

    :param config_class: configuration class
    :return: app
    """
    # Initialize Flask-

    app = Flask(__name__)
    app.config.from_object(App_Config)
    if app.config["SQLALCHEMY_DATABASE_URI"]:
        print("using db")

    # Initialize CORS
    CORS(app, supports_credentials=True)

#     # Load Swagger content from the file
#     with open("swagger_config.yaml", "r") as file:
#         swagger_config = yaml.load(file, Loader=yaml.FullLoader)
#     # Initialize Flasgger with the loaded Swagger configuration
#     Swagger(app, template=swagger_config)

    #initialize the caching system
    cache.init_app(app)

    
    # Initialize SQLAlchemy
    db.init_app(app)

    # imports blueprints
    from author_manager.authors.routes import authors
    from author_manager.books.routes import books
    from author_manager.errors.handlers import error

    # register blueprint
    app.register_blueprint(error)
    app.register_blueprint(authors)
    app.register_blueprint(books)

    # create db tables from models if not exists
    with app.app_context():
        db.create_all()

    return app