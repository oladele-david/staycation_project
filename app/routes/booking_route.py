from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime  # Import datetime module
import logging

from app.extensions import db, login_manager
from app.models import User, City, Room, Booking, Hotel, Country, State
from sqlalchemy.exc import SQLAlchemyError

booking_bp = Blueprint('booking_route', __name__)


def fetch_location_data():
    countries = Country.query.all()
    states = State.query.all()
    cities = City.query.all()
    return countries, states, cities


def calculate_total_price(room_data, check_in, check_out, no_of_rooms):
    total_days = (check_out - check_in).days
    total_price = room_data.price_per_night * total_days * no_of_rooms
    return total_days, total_price


@booking_bp.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    room_check_data = request.args
    room_id = room_check_data.get('room_id')
    check_in_date_str = room_check_data.get('check_in_date')
    check_out_date_str = room_check_data.get('check_out_date')
    no_of_adults = int(room_check_data.get('no_of_adults'))
    no_of_children = int(room_check_data.get('no_of_children'))
    no_of_rooms = int(room_check_data.get('no_of_rooms'))

    room_data = Room.query.get(room_id)
    hotel_data = Hotel.query.get(room_data.hotel_id)

    try:
        # Parse the date strings into datetime objects
        check_in = datetime.strptime(check_in_date_str, '%d-%m-%Y')
        check_out = datetime.strptime(check_out_date_str, '%d-%m-%Y')

        # Calculate the total days stayed and total price
        total_days, total_price = calculate_total_price(room_data, check_in, check_out, no_of_rooms)

    except ValueError as e:
        flash('Invalid date format. Please use dd-mm-yyyy.', 'danger')
        return redirect(url_for('room_route.get_room', room_id=room_id))

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        country_id = request.form['country']
        state_id = request.form['state']
        city_id = request.form['city']

        try:
            # Create a new booking record
            booking = Booking(
                user_id=current_user.id,
                check_in_date=check_in,
                check_out_date=check_out,
                room_id=room_id,
                total_amount=total_price,
                booking_status='Confirmed',
                hotel_id=hotel_data.id,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                address=address,
                country_id=country_id,
                state_id=state_id,
                city_id=city_id,
                no_of_rooms=no_of_rooms
            )
            db.session.add(booking)
            db.session.commit()

            flash('Booking confirmed!', 'success')
            return redirect(url_for('booking_route.confirm_booking', booking_id=booking.id))

        except SQLAlchemyError as e:
            db.session.rollback()
            logging.error(f"Database error: {e}")
            flash('An error occurred while booking. Please try again later.', 'danger')
            return redirect(url_for('room_route.get_room', room_id=room_id))
        except Exception as e:
            db.session.rollback()
            logging.error(f"Unexpected error: {e}")
            flash('An unexpected error occurred. Please try again later.', 'danger')
            return redirect(url_for('room_route.get_room', room_id=room_id))

    countries, states, cities = fetch_location_data()

    return render_template('bookings/booking.html', room_data=room_data, hotel_data=hotel_data,
                           check_in=check_in_date_str, check_out=check_out_date_str,
                           total_days=total_days, total_price=total_price,
                           no_of_adults=no_of_adults, no_of_children=no_of_children,
                           no_of_rooms=no_of_rooms, countries=countries, states=states, cities=cities)


@booking_bp.route('/confirm_booking', methods=['GET'])
@login_required
def confirm_booking():
    booking_id = request.args.get('booking_id')
    booking = Booking.query.get_or_404(booking_id)

    return render_template('bookings/confirm.html', booking=booking)
