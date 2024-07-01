# admin/facility_admin.py
from flask_admin.contrib.sqla import ModelView
from app.models.room import Room
from app.models.hotel import Hotel


class FacilityAdmin(ModelView):
    """Facility Admin View"""

    column_list = ['facility_name', 'description', 'hotel', 'created_at', 'updated_at']

    form_columns = ['facility_name', 'description', 'hotel']

    form_ajax_refs = {
        'hotel': {
            'fields': ['hotel_name'],
            'page_size': 10
        }
    }
