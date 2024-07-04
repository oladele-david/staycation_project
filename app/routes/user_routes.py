from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Booking
from app.extensions import db
from functools import wraps

user_bp = Blueprint('user_route', __name__)


@user_bp.route('/dashboard')
@login_required
def dashboard():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    pending_bookings = Booking.query.filter_by(user_id=current_user.id, booking_status='Pending').all()
    confirmed_bookings = Booking.query.filter_by(user_id=current_user.id, booking_status='Confirmed').all()
    cancelled_bookings = Booking.query.filter_by(user_id=current_user.id, booking_status='Cancelled').all()
    return render_template('users/dashboard.html', bookings=bookings, pending_bookings=pending_bookings, confirmed_bookings=confirmed_bookings, cancelled_bookings=cancelled_bookings)


@user_bp.route('/profile')
@login_required
def profile():
    pass


@user_bp.route('/update-profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    pass


@user_bp.route('/update-password', methods=['GET', 'POST'])
@login_required
def update_password():
    pass
