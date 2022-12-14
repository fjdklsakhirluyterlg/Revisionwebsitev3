"""empty message

Revision ID: b6f56727b12b
Revises: 0943c40a8bef
Create Date: 2022-12-04 08:37:02.954039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6f56727b12b'
down_revision = '0943c40a8bef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guide', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    with op.batch_alter_table('image_guide', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.Text(), nullable=True))
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=255),
               existing_nullable=False)

    with op.batch_alter_table('social_post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('content', sa.Text(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('social_post', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('content')
        batch_op.drop_column('user_id')
        batch_op.drop_column('title')

    with op.batch_alter_table('image_guide', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.String(length=255),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.drop_column('name')

    with op.batch_alter_table('guide', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')
        batch_op.drop_column('content')

    # ### end Alembic commands ###
