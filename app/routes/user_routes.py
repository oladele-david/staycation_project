from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Booking, Country, State, City
from app.extensions import db
import logging

user_bp = Blueprint('user_route', __name__)


def fetch_location_data():
    countries = Country.query.all()
    states = State.query.all()
    cities = City.query.all()
    return countries, states, cities


@user_bp.route('/dashboard')
@login_required
def dashboard():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    pending_bookings = Booking.query.filter_by(user_id=current_user.id, booking_status='Pending').all()
    confirmed_bookings = Booking.query.filter_by(user_id=current_user.id, booking_status='Confirmed').all()
    cancelled_bookings = Booking.query.filter_by(user_id=current_user.id, booking_status='Cancelled').all()
    return render_template('users/dashboard.html', bookings=bookings, pending_bookings=pending_bookings,
                           confirmed_bookings=confirmed_bookings, cancelled_bookings=cancelled_bookings)


@user_bp.route('/profile')
@login_required
def profile():
    user_profile = User.query.get(current_user.id)
    return render_template('users/profile.html', user_profile=user_profile)


@user_bp.route('/update-profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    user_profile = User.query.get(current_user.id)
    countries, states, cities = fetch_location_data()

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        other_name = request.form['other_name']
        address_line1 = request.form['address_line1']
        address_line2 = request.form['address_line2']
        city_id = request.form['city']
        state_id = request.form['state']
        country_id = request.form['country']

        user_profile.first_name = first_name
        user_profile.last_name = last_name
        user_profile.other_name = other_name
        user_profile.address_line1 = address_line1
        user_profile.address_line2 = address_line2
        user_profile.city_id = city_id
        user_profile.state_id = state_id
        user_profile.country_id = country_id

        try:
            db.session.commit()
            flash('Profile updated successfully', 'success')
            return redirect(url_for('user_route.update_profile'))

        except Exception as e:
            db.session.rollback()
            logging.error(f'Error updating profile: {e}')
            flash('An error occurred while updating your profile. Please try again later.', 'danger')
            return redirect(url_for('user_route.update_profile'))

    return render_template('users/update-profile.html', user_profile=user_profile, countries=countries, states=states,
                           cities=cities)


@user_bp.route('/update-password', methods=['GET', 'POST'])
@login_required
def update_password():
    user_profile = User.query.get(current_user.id)
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if not user_profile.check_password(current_password):
            flash('Current password is incorrect', 'danger')
            return redirect(url_for('user_route.update_password'))

        if new_password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('user_route.update_password'))

        user_profile.set_password(new_password)
        try:
            db.session.commit()
            flash('Password updated successfully', 'success')
            return redirect(url_for('user_route.update_password'))

        except Exception as e:
            db.session.rollback()
            logging.error(f'Error updating password: {e}')
            flash('An error occurred while updating your password. Please try again later.', 'danger')
            return redirect(url_for('user_route.update_password'))

    return render_template('users/update-password.html', user_profile=user_profile)
