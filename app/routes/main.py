from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    name = "Michael"
    return render_template("index.html", name=name)
    #return "Hello, this is the main route."


@main_bp.route('/about')
def about():
    return "Hello, this is the about route."
