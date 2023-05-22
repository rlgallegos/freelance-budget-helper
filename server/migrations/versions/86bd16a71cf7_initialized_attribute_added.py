"""initialized attribute added

Revision ID: 86bd16a71cf7
Revises: 6be79d5bdb0c
Create Date: 2023-05-21 05:22:55.926995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86bd16a71cf7'
down_revision = '6be79d5bdb0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('initialized', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('initialized')

    # ### end Alembic commands ###