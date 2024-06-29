from flask import Flask
import pymysql
from flask_admin.contrib.sqla import ModelView

pymysql.install_as_MySQLdb()

from .extensions import db, migrate, login_manager
from .routes import main_bp, user_bp, hotel_bp, room_bp
from app.routes.auth import auth_bp
from .admin.initialize_admin import initialize_admin


def create_app():
    """Construct the core application."""

    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Initialize Flask-Admin
    initialize_admin(app)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(hotel_bp, url_prefix='/hotels')
    app.register_blueprint(room_bp, url_prefix='/rooms')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
