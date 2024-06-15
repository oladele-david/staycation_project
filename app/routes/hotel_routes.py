from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import Hotel
from app.extensions import db

hotel_bp = Blueprint('hotel', __name__)


@hotel_bp.route('/')
def get_hotels():
    hotels = [{"name": "Hotel 1", "location": "Location 1"},{"name": "Hotel 2", "location": "Location 2"}]
    return render_template("hotels.html", hotels=hotels)

@hotel_bp.route('/add')
def add_hotel():
    return "Add Hotel Endpoint"
