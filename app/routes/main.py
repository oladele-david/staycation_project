from flask import Blueprint, render_template
from flask_login import current_user
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        name = current_user.username  # Assuming 'username' is an attribute of your User model
        email = current_user.email
    else:
        name = "Guest"
        email = None

    return render_template("main/index.html", name=name, email=email)
    #return "Hello, this is the main route."


@main_bp.route('/about')
def about():
    if current_user.is_authenticated:
        name = current_user.username  # Assuming 'username' is an attribute of your User model
        email = current_user.email
    else:
        name = "Guest"
        email = None
    return render_template("main/about.html", name=name, email=email)


@main_bp.route('/contact')
def contact():
    return render_template("main/contact.html")

