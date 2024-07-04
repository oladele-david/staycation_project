from datetime import datetime
from app.extensions import db
import random
import string


class Booking(db.Model):
    """Booking model for storing bookings related details."""

    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.String(10), unique=True, nullable=False)  # New unique booking ID
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_amount = db.Column(db.Float, nullable=False)
    booking_status = db.Column(db.String(64), nullable=False)
    no_of_rooms = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'), nullable=False)

    # Relationships
    user = db.relationship('User', back_populates='bookings')
    room = db.relationship('Room', back_populates='bookings')
    hotel = db.relationship('Hotel', back_populates='bookings')
    country = db.relationship('Country', back_populates='bookings')
    state = db.relationship('State', back_populates='bookings')
    city = db.relationship('City', back_populates='bookings')

    def __repr__(self):
        return f'<Booking {self.booking_id}, {self.user_id}>'

    def generate_booking_id(self):
        """Generate a unique 10-digit booking ID."""
        while True:
            booking_id = ''.join(random.choices(string.digits, k=10))
            if not Booking.query.filter_by(booking_id=booking_id).first():
                return booking_id

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.booking_id:
            self.booking_id = self.generate_booking_id()
