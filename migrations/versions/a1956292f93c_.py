"""empty message

Revision ID: a1956292f93c
Revises: fbb9b5f4f930
Create Date: 2020-03-27 21:33:55.823525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1956292f93c'
down_revision = 'fbb9b5f4f930'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    op.drop_column('users', 'role1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role1', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.create_table('test',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='test_pkey')
    )
    # ### end Alembic commands ###
