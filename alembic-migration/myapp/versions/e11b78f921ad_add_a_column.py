"""add a column

Revision ID: e11b78f921ad
Revises: eeb207c3a636
Create Date: 2024-10-09 14:04:01.458602

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'e11b78f921ad'
down_revision: Union[str, None] = 'eeb207c3a636'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade() -> None:
    op.drop_column('account', 'last_transaction_date')
