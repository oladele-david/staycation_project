"""Change id field to UUID4 in User model

Revision ID: 237b50f6e99d
Revises: 15dd319d8634
Create Date: 2024-06-28 01:41:55.632974

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '237b50f6e99d'
down_revision = '15dd319d8634'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=36),
               existing_nullable=False)
        op.drop_constraint('bookings_ibfk_1', 'bookings', type_='foreignkey')
        op.drop_constraint('bookings_ibfk_2', 'bookings', type_='foreignkey')
        op.drop_constraint('bookings_ibfk_3', 'bookings', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.String(length=36),
               type_=mysql.INTEGER(),
               existing_nullable=False)
        op.create_foreign_key('bookings_ibfk_1', 'bookings', 'users', ['user_id'], ['id'])
        op.create_foreign_key('bookings_ibfk_2', 'bookings', 'rooms', ['room_id'], ['id'])
        op.create_foreign_key('bookings_ibfk_3', 'bookings', 'hotels', ['hotel_id'], ['id'])

    # ### end Alembic commands ###
