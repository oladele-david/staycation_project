from datetime import datetime
from app.extensions import db


class Hotel(db.Model):
    """Hotel model for storing hotel related details."""

    __tablename__ = 'hotels'
    id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(128), nullable=False)  # Specify length
    address = db.Column(db.String(256), nullable=False)  # Specify length
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    postcode = db.Column(db.String(20), nullable=False)  # Specify length
    rating = db.Column(db.Float)
    contact_number = db.Column(db.String(20), nullable=False)  # Specify length
    email = db.Column(db.String(120), nullable=False)  # Specify length
    description = db.Column(db.String(512))  # Specify length
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    rooms = db.relationship('Room', back_populates='hotel', lazy=True)
    bookings = db.relationship('Booking', back_populates='hotel', lazy=True)
    facilities = db.relationship('Facility', back_populates='hotel', lazy=True)
    rules = db.relationship('Rule', back_populates='hotel', lazy=True)
    country = db.relationship('Country', back_populates='hotels')
    state = db.relationship('State', back_populates='hotels')
    city = db.relationship('City', back_populates='hotels')

    def __repr__(self):
        return f"<Hotel '{self.hotel_name}'>"
