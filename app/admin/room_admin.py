# admin/room_admin.py
from flask_admin.contrib.sqla import ModelView
from app.models.room import Room
from app.models.hotel import Hotel


class RoomAdmin(ModelView):
    """Room Admin View"""

    column_list = ['room_number', 'room_type', 'description', 'size', 'number_of_beds',
                   'max_adults', 'max_children', 'number_of_rooms_available', 'price_per_night',
                   'status', 'hotel']

    form_columns = ['room_number', 'room_type', 'description', 'size', 'number_of_beds',
                    'max_adults', 'max_children', 'number_of_rooms_available', 'price_per_night',
                    'status', 'hotel']

    form_ajax_refs = {
        'hotel': {
            'fields': (Hotel.hotel_name,),
            'page_size': 10
        }
    }
    