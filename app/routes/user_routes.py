from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app.extensions import db
from functools import wraps

user_bp = Blueprint('user_route', __name__)


@user_bp.route('/')
def get_users():
    # Sample response, replace with actual implementation
    return jsonify({"message": "List of users"}), 200


@user_bp.route('/register')
def register():
    return "Register Endpoint"


@user_bp.route('/login')
def login():
    return "Login Endpoint"


@user_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function


@user_bp.route('/admin')
@login_required
@admin_required
def admin():
    return "Admin Endpoint"
