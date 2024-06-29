# admin/hotel_admin.py
from flask_admin.contrib.sqla import ModelView
from app.models.hotel import Hotel
from app.models.city import City
from app.models.state import State
from app.models.country import Country

class HotelAdmin(ModelView):
    column_list = ['hotel_name', 'address', 'city', 'state', 'country', 'postcode',
                   'rating', 'contact_number', 'email', 'description', 'created_at', 'updated_at']

    form_columns = ['hotel_name', 'address', 'city', 'state', 'country', 'postcode',
                    'rating', 'contact_number', 'email', 'description']

    form_ajax_refs = {
        'city': {
            'fields': ['name'],
            'page_size': 10
        },
        'state': {
            'fields': ['name'],
            'page_size': 10
        },
        'country': {
            'fields': ['name'],
            'page_size': 10
        }
    }
