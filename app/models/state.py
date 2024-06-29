from datetime import datetime
from app.extensions import db


class State(db.Model):
    """State model for storing state related details."""

    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    cities = db.relationship('City', back_populates='state', lazy=True)
    country = db.relationship('Country', back_populates='states')
    users = db.relationship('User', back_populates='state')
    hotels = db.relationship('Hotel', back_populates='state')

    def __repr__(self):
        return f"<State '{self.name}'>"
