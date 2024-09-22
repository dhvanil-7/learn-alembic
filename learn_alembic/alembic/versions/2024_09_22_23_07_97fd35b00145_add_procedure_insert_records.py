"""add_procedure_insert_records

Revision ID: 97fd35b00145
Revises: 548bc6f5fc0e
Create Date: 2024-09-22 23:07:11.032613+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision: str = '97fd35b00145'
down_revision: Union[str, None] = '548bc6f5fc0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE OR ALTER PROCEDURE dbo.insert_records
            AS
            BEGIN
                INSERT INTO dbo.first_table(name, address, height_cm, weight_kg)
                VALUES ('a', 'b', 170, 65),
                ('c', 'f', 155, 58),
                ('d', 'g', 175, 80),
                ('e', 'h', 185, 77.8)
            END;
    """)
    op.execute("EXEC dbo.insert_records;")


def downgrade() -> None:
    op.execute("""DROP PROCEDURE dbo.insert_records""")
