from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from app.extensions import db, login_manager
from app.models import User
from sqlalchemy.exc import SQLAlchemyError

auth_bp = Blueprint('auth_route', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = User.query.filter_by(email=email).first()

            if user is None or not user.check_password(password):
                flash('Invalid email or password', 'danger')
                return redirect(url_for('auth.login'))
            else:
                login_user(user)
                flash('You have been logged in.', 'success')
                return redirect(url_for('main_route.index'))

        except SQLAlchemyError as e:
            flash('An error occurred while accessing the database. Please try again later.', 'danger')
            return redirect(url_for('auth_route.login'))

        except Exception as e:
            flash('An unexpected error occurred. Please try again later.', 'danger')
            return redirect(url_for('auth_route.login'))

    return render_template('auth/login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('auth.register'))

        try:
            if User.query.filter_by(phone=phone).first():
                flash('Phone already exists', 'danger')
                return redirect(url_for('auth.register'))

            if User.query.filter_by(email=email).first():
                flash('Email already exists', 'danger')
                return redirect(url_for('auth.register'))

            user = User(first_name=first_name, last_name=last_name, email=email, phone=phone)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('auth.login'))

        except SQLAlchemyError as e:
            db.session.rollback()  # Rollback the session in case of error
            flash('An error occurred while accessing the database. Please try again later.', 'danger')
            return redirect(url_for('auth.register'))

        except Exception as e:
            db.session.rollback()  # Rollback the session in case of error
            flash('An unexpected error occurred. Please try again later.', 'danger')
            return redirect(url_for('auth.register'))

    return render_template('auth/register.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main_route.index'))
