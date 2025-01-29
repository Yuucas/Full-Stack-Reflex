"""empty message

Revision ID: 596f55a2b8fc
Revises: bb355884b3ce
Create Date: 2025-01-29 10:20:16.121239

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '596f55a2b8fc'
down_revision: Union[str, None] = 'bb355884b3ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacentrymodel', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacentrymodel', schema=None) as batch_op:
        batch_op.drop_column('create_date')

    # ### end Alembic commands ###
