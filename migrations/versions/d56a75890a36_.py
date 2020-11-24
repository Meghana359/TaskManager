"""empty message

Revision ID: d56a75890a36
Revises: 
Create Date: 2020-11-24 01:47:27.711831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd56a75890a36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Assignment', sa.Column('ifDone', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Assignment', 'ifDone')
    # ### end Alembic commands ###
