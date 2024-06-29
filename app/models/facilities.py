from datetime import datetime
from app.extensions import db


class Facility(db.Model):
    """Facility model for storing facility related details."""

    __tablename__ = 'facilities'
    id = db.Column(db.Integer, primary_key=True)
    facility_name = db.Column(db.String(128), nullable=False)  # Specify length
    description = db.Column(db.String(256))  # Specify length
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    hotel = db.relationship('Hotel', back_populates='facilities')
