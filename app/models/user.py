from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.extensions import db


class User(UserMixin, db.Model):
    """User model for storing user related details"""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    other_name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=True, unique=True)
    password_hash = db.Column(db.String(128))
    address_line1 = db.Column(db.String(255))
    address_line2 = db.Column(db.String(255))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=True)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=True)
    zip_code = db.Column(db.String(20))
    country = db.relationship('Country', backref='user', lazy=True)
    state = db.relationship('State', backref='user', lazy=True)
    city = db.relationship('City', backref='user', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.first_name}>, {self.email}, {self.created_at}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
