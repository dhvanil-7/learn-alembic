"""add_column

Revision ID: 6078b2d55f8c
Revises: d26a94780e43
Create Date: 2024-07-16 18:03:48.361623+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6078b2d55f8c'
down_revision: Union[str, None] = 'd26a94780e43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        ALTER TABLE first_table ADD phone VARCHAR(15)
    """)
    pass


def downgrade() -> None:
    op.execute("""
        ALTER TABLE first_table DROP COLUMN phone
    """)
    pass
