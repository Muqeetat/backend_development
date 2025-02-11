"""create users table

Revision ID: 3c7aa82b8ca9
Revises: ef702d9f7cff
Create Date: 2025-02-11 16:21:50.138944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = '3c7aa82b8ca9'
down_revision: Union[str, None] = 'ef702d9f7cff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('name', sa.String(50), nullable=False, unique=True),
        sa.Column('password', sa.Text, nullable=False),
        sa.Column('create_date', sa.TIMESTAMP, nullable=False, server_default=func.now())
    )
    pass

def downgrade()-> None:
    op.drop_table('users')
    pass
