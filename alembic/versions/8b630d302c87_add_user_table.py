"""add user table

Revision ID: 8b630d302c87
Revises: 7cd83682cb01
Create Date: 2026-08-05 11:30:40.105377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b630d302c87'
down_revision: Union[str, Sequence[str], None] = '7cd83682cb01'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
                    sa.Column('email', sa.String(), nullable=False, unique=True), 
                    sa.Column('password', sa.String(), nullable=False), 
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False)
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
