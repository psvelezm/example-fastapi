"""add content column to posts table

Revision ID: 7cd83682cb01
Revises: 319cff292d9a
Create Date: 2026-08-05 11:12:59.336020

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7cd83682cb01'
down_revision: Union[str, Sequence[str], None] = '319cff292d9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))   

    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
