from flask import Blueprint, render_template
from flask_login import current_user
from app.models import User
from app.models import City

main_bp = Blueprint('main_route', __name__)


@main_bp.route('/')
def index():
    locations = City.query.all()

    return render_template("main/index.html", locations=locations)
    #return "Hello, this is the main route."


@main_bp.route('/about')
def about():
    return render_template("main/about.html")


@main_bp.route('/contact')
def contact():
    return render_template("main/contact.html")
