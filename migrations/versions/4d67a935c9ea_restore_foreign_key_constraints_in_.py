"""Restore foreign key constraints in bookings table

Revision ID: 4d67a935c9ea
Revises: e7e6f55b7961
Create Date: 2024-06-28 02:05:36.829411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d67a935c9ea'
down_revision = 'e7e6f55b7961'
branch_labels = None
depends_on = None


def upgrade():
    # Restore the foreign key constraints
    op.create_foreign_key('bookings_ibfk_1', 'bookings', 'users', ['user_id'], ['id'])
    op.create_foreign_key('bookings_ibfk_2', 'bookings', 'rooms', ['room_id'], ['id'])
    op.create_foreign_key('bookings_ibfk_3', 'bookings', 'hotels', ['hotel_id'], ['id'])
    # Repeat for all foreign keys


def downgrade():
    # Drop the foreign key constraints, if needed.
    op.drop_constraint('bookings_ibfk_1', 'bookings', type_='foreignkey')
    op.drop_constraint('bookings_ibfk_2', 'bookings', type_='foreignkey')
    op.drop_constraint('bookings_ibfk_3', 'bookings', type_='foreignkey')

    # ### end Alembic commands ###
