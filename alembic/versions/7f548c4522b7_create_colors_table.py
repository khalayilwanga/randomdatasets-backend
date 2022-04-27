"""CREATE_COLORS_TABLE

Revision ID: 7f548c4522b7
Revises: 1e545f0a8644
Create Date: 2021-10-01 14:39:32.338936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f548c4522b7'
down_revision = '1e545f0a8644'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('colores',
                    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column('red', sa.Integer, nullable=False),
                    sa.Column('blue', sa.Integer, nullable=False),
                    sa.Column('green', sa.Integer, nullable=False),
                    sa.Column('alpha', sa.Integer, nullable=False),
                    )


def downgrade():
    op.drop_table('colores')
