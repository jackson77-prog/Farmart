from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

db = SQLAlchemy()
migrate = Migrate()  # Initialize Migrate

def create_app(config_class='app.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app, resources={r"*": {"origins": app.config['CORS_ORIGINS']}})
    db.init_app(app)
    migrate.init_app(app, db)  # Initialize Migrate with app and db

    with app.app_context():
        db.create_all()

    # Import and register blueprints
    from app.routes import register_routes
    register_routes(app)

    return app
