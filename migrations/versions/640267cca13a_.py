"""empty message

Revision ID: 640267cca13a
Revises: ae04783ad4f3
Create Date: 2022-11-23 20:33:45.094974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '640267cca13a'
down_revision = 'ae04783ad4f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('image_card', schema=None) as batch_op:
        batch_op.add_column(sa.Column('filename', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('image_card', schema=None) as batch_op:
        batch_op.drop_column('created_at')
        batch_op.drop_column('filename')

    # ### end Alembic commands ###
