"""Ativo

Revision ID: f593f0ca0c55
Revises: 74964cf87b89
Create Date: 2022-05-24 08:43:42.469681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f593f0ca0c55'
down_revision = '74964cf87b89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cgp_colaborador', sa.Column('active', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cgp_colaborador', 'active')
    # ### end Alembic commands ###
