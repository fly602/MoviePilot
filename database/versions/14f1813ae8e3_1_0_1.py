"""1.0.1

Revision ID: 14f1813ae8e3
Revises: 9f4edd55c2d4
Create Date: 2023-07-27 12:34:57.839443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14f1813ae8e3'
down_revision = '9f4edd55c2d4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        with op.batch_alter_table("subscribe") as batch_op:
            batch_op.add_column(sa.Column('best_version', sa.Integer, nullable=True))
            batch_op.add_column(sa.Column('current_priority', sa.Integer, nullable=True))
    except Exception as e:
        pass
    # ### end Alembic commands ###


def downgrade() -> None:
    pass
