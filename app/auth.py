from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import User
from app.extensions import db, login_manager

auth_bp = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_bp.route('/login')
def login():
    return "Login Auth Endpoint"
