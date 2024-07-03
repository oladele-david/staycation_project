from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from app.models import City
from app.models import Room

room_bp = Blueprint('room_route', __name__)


@room_bp.route('/')
def get_rooms():
    locations = City.query.all()
    hotel_rooms = Room.query.all()
    return render_template("rooms/rooms.html", locations=locations, hotel_rooms=hotel_rooms)


@room_bp.route('/single/<int:room_id>')
def get_room(room_id):
    try:
        room_id = int(room_id)
        room_data = Room.query.get(room_id)
        if room_data is None:
            flash("Room not found", "danger")
            return redirect(url_for('room_route.get_rooms'))
    except ValueError:
        flash("Invalid room id", "danger")
        return redirect(url_for('room_route.get_rooms'))

    return render_template("rooms/single.html", room_data=room_data)


@room_bp.route('/book', methods=['GET', 'POST'])
def book_room():
    pass

