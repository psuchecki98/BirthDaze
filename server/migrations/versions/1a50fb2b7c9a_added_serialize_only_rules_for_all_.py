"""Added serialize_only rules for all Models except Tag/BirthdayTags

Revision ID: 1a50fb2b7c9a
Revises: 0b790e2ebc1b
Create Date: 2023-08-02 11:49:44.783368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a50fb2b7c9a'
down_revision = '0b790e2ebc1b'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
