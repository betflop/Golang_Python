"""empty message

Revision ID: 217b19afff73
Revises: 0fd13895bad8
Create Date: 2023-12-26 00:00:39.331137

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '217b19afff73'
down_revision: Union[str, None] = '0fd13895bad8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('text', sa.String(), nullable=True))
    op.add_column('questions', sa.Column('answer', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questions', 'answer')
    op.drop_column('questions', 'text')
    # ### end Alembic commands ###
