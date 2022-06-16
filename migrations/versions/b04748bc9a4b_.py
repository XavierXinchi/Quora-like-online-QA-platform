"""empty message

Revision ID: b04748bc9a4b
Revises: 6cb9f1baa84b
Create Date: 2022-06-15 15:51:37.073072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b04748bc9a4b'
down_revision = '6cb9f1baa84b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'create_time')
    # ### end Alembic commands ###