"""create tasks table

Revision ID: ef702d9f7cff
Revises: 
Create Date: 2025-02-11 16:16:37.982790

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = 'ef702d9f7cff'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('category', sa.String(50), server_default='personal',nullable=False),
        sa.Column('status', sa.String(50), server_default='in-progress',nullable=False),
        sa.Column('due_date', sa.TIMESTAMP, nullable=True),
        sa.Column('create_date', sa.TIMESTAMP, nullable=False, server_default=func.now()),
        sa.Column('update_date', sa.TIMESTAMP, nullable=True, onupdate=func.now())
    )
    pass

def downgrade()-> None:
    op.drop_table('tasks')
    pass
