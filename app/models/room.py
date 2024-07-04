from app.extensions import db


class Room(db.Model):
    """Room model for storing room related details."""

    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(10), nullable=False)
    room_type = db.Column(db.String(128), nullable=False)  # Specify length
    description = db.Column(db.String(512))  # Specify length
    size = db.Column(db.String(64), nullable=False)  # Specify length
    number_of_beds = db.Column(db.Integer, nullable=False)
    max_adults = db.Column(db.Integer, nullable=False)
    max_children = db.Column(db.Integer, nullable=False)
    number_of_rooms_available = db.Column(db.Integer, nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(64), nullable=False)  # Specify length
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'), nullable=False)
    bookings = db.relationship('Booking', back_populates='room', lazy=True)
    hotel = db.relationship('Hotel', back_populates='rooms')

    def __repr__(self):
        return f"<Room '{self.room_type}'>"
