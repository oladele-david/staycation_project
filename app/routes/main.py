from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return "Hello, this is the main route."


@main_bp.route('/about')
def about():
    return "Hello, this is the about route."
