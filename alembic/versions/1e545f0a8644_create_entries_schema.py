"""“create_entries_schema”

Revision ID: 1e545f0a8644
Revises: 
Create Date: 2021-09-26 01:43:31.617254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e545f0a8644'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('entries',
     sa.Column('id',sa.Integer,primary_key=True, autoincrement=True),
     sa.Column('value', sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table('entries')
