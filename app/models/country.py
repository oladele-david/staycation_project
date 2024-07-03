from datetime import datetime
from app.extensions import db


class Country(db.Model):
    """Country model for storing country related details."""

    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    code = db.Column(db.String(8), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    states = db.relationship('State', back_populates='country', lazy=True)
    users = db.relationship('User', back_populates='country', lazy=True)
    hotels = db.relationship('Hotel', back_populates='country', lazy=True)
    bookings = db.relationship('Booking', back_populates='country', lazy=True)

    def __repr__(self):
        return f"<Country '{self.name}'>"
