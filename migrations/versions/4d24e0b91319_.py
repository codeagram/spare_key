"""empty message

Revision ID: 4d24e0b91319
Revises: 6a98c0a01f85
Create Date: 2021-07-28 20:20:20.457276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d24e0b91319'
down_revision = '6a98c0a01f85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spare_key', sa.Column('expected_date_of_return', sa.Date(), nullable=True))
    op.add_column('spare_key', sa.Column('returned_date', sa.Date(), nullable=True))
    op.drop_column('spare_key', 'return_date')
    op.drop_column('spare_key', 'Expected_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spare_key', sa.Column('Expected_date', sa.DATE(), nullable=True))
    op.add_column('spare_key', sa.Column('return_date', sa.DATE(), nullable=True))
    op.drop_column('spare_key', 'returned_date')
    op.drop_column('spare_key', 'expected_date_of_return')
    # ### end Alembic commands ###
