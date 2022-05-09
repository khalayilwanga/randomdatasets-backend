"""“create_entries_schema”

Revision ID: 1e545f0a8644
Revises: 
Create Date: 2021-09-26 01:43:31.617254

"""
from alembic import op
import os
import sqlalchemy as sa

# dynamically setting database url
MYSQL_USER =os.environ['MYSQL_USER']
MYSQL_DB =os.environ['MYSQL_DB']
MYSQL_PASSWORD=os.environ['MYSQL_PASSWORD']
#
e = sa.create_engine(f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@db/{MYSQL_DB}')


# revision identifiers, used by Alembic.
revision = '1e545f0a8644'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    if sa.inspect(e,).has_table("entries") == True:
        return
    else:
        op.create_table('entries',
                        sa.Column('id',sa.Integer,primary_key=True, autoincrement=True),
                        sa.Column('value', sa.Integer, nullable=False),
                        )


def downgrade():
    op.drop_table('entries')
