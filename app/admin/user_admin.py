# admin/user_admin.py
from flask_admin.contrib.sqla import ModelView
from app.models.user import User
from app.models.country import Country
from app.models.state import State
from app.models.city import City


class UserAdmin(ModelView):
    # Columns to display in list view
    column_list = ('first_name', 'last_name', 'email', 'country', 'state', 'city')

    # Fields to display in the form
    form_columns = ['first_name', 'last_name', 'other_name', 'email', 'phone', 'password_hash',
                    'address_line1', 'address_line2', 'zip_code', 'country', 'state', 'city', 'is_admin']

    # AJAX loading for related fields
    form_ajax_refs = {
        'country': {
            'fields': (Country.name,), 'page_size': 10
        },
        'state': {
            'fields': (State.name,), 'page_size': 10
        },
        'city': {
            'fields': (City.name,), 'page_size': 10
        }
    }
