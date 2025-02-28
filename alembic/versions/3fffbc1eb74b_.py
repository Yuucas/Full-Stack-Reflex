"""empty message

Revision ID: 3fffbc1eb74b
Revises: 2ecbee15c261
Create Date: 2025-01-30 11:27:01.977421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '3fffbc1eb74b'
down_revision: Union[str, None] = '2ecbee15c261'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogpostmodel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('content', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('create_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('update_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogpostmodel')
    # ### end Alembic commands ###
