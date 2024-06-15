from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import Hotel
from app.extensions import db

hotel_bp = Blueprint('hotel', __name__)


@hotel_bp.route('/')
def get_hotels():
    return "List of hotels"


@hotel_bp.route('/add')
def add_hotel():
    return "Add Hotel Endpoint"
