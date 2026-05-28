"""add_hashed_password

Revision ID: fc461064a1ac
Revises: 400421011e8b
Create Date: 2026-05-29 00:30:03.887417

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc461064a1ac'
down_revision: Union[str, Sequence[str], None] = '400421011e8b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
