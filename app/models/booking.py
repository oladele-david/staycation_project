from datetime import datetime
from app.extensions import db


class Booking(db.Model):
    """Booking model for storing bookings related details."""

    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)
    booking_status = db.Column(db.String(64), nullable=False)
    special_requirements = db.Column(db.String(256))
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'), nullable=False)
    user = db.relationship('User', back_populates='bookings')
    room = db.relationship('Room', back_populates='bookings')
    hotel = db.relationship('Hotel', back_populates='bookings')
