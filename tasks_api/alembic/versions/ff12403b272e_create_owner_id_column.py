"""create owner_id column

Revision ID: ff12403b272e
Revises: 3c7aa82b8ca9
Create Date: 2025-02-11 16:32:08.683898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff12403b272e'
down_revision: Union[str, None] = '3c7aa82b8ca9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('tasks', sa.Column('owner_id', sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False))
    pass

def downgrade() -> None:
    op.drop_column('tasks', 'owner_id')
    pass