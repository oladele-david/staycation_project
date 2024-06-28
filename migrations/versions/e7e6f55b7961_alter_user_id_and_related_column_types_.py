"""Alter user_id and related column types in bookings table and id in users table

Revision ID: e7e6f55b7961
Revises: 237b50f6e99d
Create Date: 2024-06-28 02:03:18.758386

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e7e6f55b7961'
down_revision = '237b50f6e99d'
branch_labels = None
depends_on = None


def upgrade():
    # Alter columns to the same type
    op.alter_column('users', 'id',
                    existing_type=sa.Integer(),
                    type_=sa.String(length=36),
                    existing_nullable=False)

    op.alter_column('bookings', 'user_id',
                    existing_type=sa.Integer(),
                    type_=sa.String(length=36),
                    existing_nullable=False)  # Adjust nullable as per your requirement


def downgrade():
    # Revert column alterations
    op.alter_column('users', 'id',
                    existing_type=sa.String(length=36),
                    type_=sa.Integer(),
                    existing_nullable=False)

    op.alter_column('bookings', 'user_id',
                    existing_type=sa.String(length=36),
                    type_=sa.Integer(),
                    existing_nullable=False)
    # ### end Alembic commands ###
