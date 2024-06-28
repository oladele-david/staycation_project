from flask import Blueprint, render_template
from flask_login import current_user

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template("main/index.html")
    #return "Hello, this is the main route."


@main_bp.route('/about')
def about():
    return render_template("main/about.html")


@main_bp.route('/contact')
def contact():
    return render_template("main/contact.html")
