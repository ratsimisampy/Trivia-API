"""add genre


Revision ID: f5bdbe5dfe04
Revises: e7f5646c749c
Create Date: 2020-07-01 23:09:52.782405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5bdbe5dfe04'
down_revision = 'e7f5646c749c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
    op.drop_column('Venue', 'website')
    op.drop_column('Venue', 'quote')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('quote', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.add_column('Venue', sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###
