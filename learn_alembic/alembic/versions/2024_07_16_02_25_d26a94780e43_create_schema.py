"""create_schema

Revision ID: d26a94780e43
Revises: 
Create Date: 2024-07-16 02:25:19.649893+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd26a94780e43'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
                CREATE TABLE first_table (
                    id UNIQUEIDENTIFIER default NEWID(),
                    name VARCHAR(MAX),
                    address VARCHAR(MAX),
                    height_cm INTEGER,
                    weight_kg DECIMAL(4,1),
                    bmi DECIMAL(4,1)
                    CONSTRAINT first_table_primary_key_id PRIMARY KEY (id)
                )
    """)
    pass


def downgrade() -> None:
    op.execute("""
                DROP TABLE dbo.first_table
    """)
    pass
