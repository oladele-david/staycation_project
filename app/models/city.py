from datetime import datetime
from app.extensions import db


class City(db.Model):
    """City model for storing city related details."""

    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    state = db.relationship('State', back_populates='cities')
    users = db.relationship('User', back_populates='city')
    hotels = db.relationship('Hotel', back_populates='city')

    def __repr__(self):
        return f"<City '{self.name}'>"
