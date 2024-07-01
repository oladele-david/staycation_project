# admin/initialize_admin.py
from flask_admin import Admin
from .secure_admin import SecureModelView, SecureAdminIndexView
from .user_admin import UserAdmin
from .hotel_admin import HotelAdmin
from .room_admin import RoomAdmin
from .facility_admin import FacilityAdmin
from app.extensions import db
from app.models.user import User
from app.models.booking import Booking
from app.models.hotel import Hotel
from app.models.country import Country
from app.models.state import State
from app.models.city import City
from app.models.room import Room
from app.models.facilities import Facility


def initialize_admin(app):
    admin = Admin(
        app,
        name='Staycation',
        template_mode='bootstrap4',
        index_view=SecureAdminIndexView()
    )
    admin.add_view(UserAdmin(User, db.session))  # Use the custom UserAdmin class
    admin.add_view(HotelAdmin(Hotel, db.session))  # Use the custom HotelAdmin class
    admin.add_view(RoomAdmin(Room, db.session))
    admin.add_view(FacilityAdmin(Facility,db.session))

    admin.add_view(SecureModelView(Booking, db.session))
    admin.add_view(SecureModelView(Country, db.session))
    admin.add_view(SecureModelView(State, db.session))
    admin.add_view(SecureModelView(City, db.session))
