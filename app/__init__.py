from flask import Flask
import pymysql

pymysql.install_as_MySQLdb()
from .extensions import db, migrate, login_manager
from .routes import main_bp, user_bp, hotel_bp, room_bp
from .auth import auth_bp


def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(hotel_bp, url_prefix='/hotels')
    app.register_blueprint(room_bp, url_prefix='/rooms')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
