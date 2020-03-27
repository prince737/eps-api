"""empty message

Revision ID: fbb9b5f4f930
Revises: 
Create Date: 2020-03-27 20:52:02.683240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbb9b5f4f930'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('password', sa.String(length=512), nullable=False),
    sa.Column('dob', sa.DateTime(), nullable=False),
    sa.Column('email', sa.String(length=512), nullable=True),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('phone', sa.String(length=10), nullable=False),
    sa.Column('image', sa.String(length=512), nullable=True),
    sa.Column('role', sa.String(length=128), nullable=True),
    sa.Column('role1', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('test')
    # ### end Alembic commands ###