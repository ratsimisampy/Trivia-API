"""venue_shows init

Revision ID: 6659e2091d12
Revises: 6e8019929326
Create Date: 2020-06-29 20:50:51.556065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6659e2091d12'
down_revision = '6e8019929326'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venue_shows',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('booking_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('artist_id', 'venue_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venue_shows')
    # ### end Alembic commands ###
