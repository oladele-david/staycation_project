from flask import Blueprint, render_template, redirect, url_for, flash

room_bp = Blueprint('room', __name__)


@room_bp.route('/')
def get_rooms():
    return "List of rooms"


@room_bp.route('/<int:room_id>')
def get_room(room_id):
    return f"you are access a Room with  {room_id}"


