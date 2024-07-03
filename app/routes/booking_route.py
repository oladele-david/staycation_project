from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime, timedelta  # Import datetime module

from app.extensions import db, login_manager
from app.models import User, City, Room, Booking, Hotel, Country, State
from sqlalchemy.exc import SQLAlchemyError

booking_bp = Blueprint('booking_route', __name__)


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
    # Parse the date strings into datetime objects
    check_in = datetime.strptime(check_in_date_str, '%d-%m-%Y')
    check_out = datetime.strptime(check_out_date_str, '%d-%m-%Y')

    # Calculate the total days stayed
    total_days = (check_out - check_in).days
    total_price = room_data.price_per_night * total_days * no_of_rooms

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
            # Parse the date strings into datetime objects
            check_in = datetime.strptime(check_in_date_str, '%d-%m-%Y')
            check_out = datetime.strptime(check_out_date_str, '%d-%m-%Y')

            # Calculate the total days stayed
            total_days = (check_out - check_in).days

            if total_days <= 0:
                raise ValueError("Check-out date must be after check-in date.")

            # Calculate the total price
            total_price = room_data.price_per_night * total_days * no_of_rooms

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
                no_of_rooms=no_of_rooms  # Add no_of_rooms to the booking
            )
            db.session.add(booking)
            db.session.commit()

            flash('Booking confirmed!', 'success')
            return redirect(url_for('booking.index'))

        except ValueError as e:
            flash('Invalid date format. Please use dd-mm-yyyy.', 'danger')
            return redirect(url_for('room_route.get_room', room_id=room_id))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash('An error occurred while booking. Please try again later.', 'danger')
            return redirect(url_for('room_route.get_room', room_id=room_id))
        except Exception as e:
            db.session.rollback()
            flash('An unexpected error occurred. Please try again later.', 'danger')
            return redirect(url_for('room_route.get_room', room_id=room_id))

    countries = Country.query.all()
    states = State.query.all()
    cities = City.query.all()

    return render_template('bookings/booking.html', room_data=room_data, hotel_data=hotel_data,
                           check_in=check_in_date_str, check_out=check_out_date_str,
                           total_days=total_days, total_price=total_price,
                           no_of_adults=no_of_adults, no_of_children=no_of_children,
                           no_of_rooms=no_of_rooms, countries=countries, states=states, cities=cities)

