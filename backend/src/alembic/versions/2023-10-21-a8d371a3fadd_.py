"""empty message

Revision ID: a8d371a3fadd
Revises: ed446c8e18d9
Create Date: 2023-10-21 18:07:41.417398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8d371a3fadd'
down_revision = 'ed446c8e18d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('care_postulation', sa.Column('allowed_specie', sa.Enum('dog', 'cat', name='species'), nullable=False))
    op.drop_column('care_postulation', 'allowed_species')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('care_postulation', sa.Column('allowed_species', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('care_postulation', 'allowed_specie')
    # ### end Alembic commands ###
