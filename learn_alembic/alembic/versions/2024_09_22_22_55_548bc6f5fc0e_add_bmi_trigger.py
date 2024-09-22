"""add_bmi_trigger

Revision ID: 548bc6f5fc0e
Revises: 6078b2d55f8c
Create Date: 2024-09-22 22:55:49.774833+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision: str = '548bc6f5fc0e'
down_revision: Union[str, None] = '6078b2d55f8c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
            CREATE OR ALTER TRIGGER dbo.calc_bmi
                ON learn_alembic.dbo.first_table
                AFTER INSERT
                AS
                BEGIN
                    UPDATE learn_alembic.dbo.first_table
                    SET bmi = (weight_kg / (height_cm*height_cm))*10000
                END;
        """
    )


def downgrade() -> None:
    op.execute("""
        DROP TRIGGER dbo.calc_bmi
        """)
