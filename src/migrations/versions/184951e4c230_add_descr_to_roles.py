"""add descr to roles

Revision ID: 184951e4c230
Revises: c7102203f0f7
Create Date: 2021-10-26 21:51:14.922801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '184951e4c230'
down_revision = 'c7102203f0f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
