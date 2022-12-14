"""empty message

Revision ID: 1f5a89776d38
Revises: 32cdd06111c0
Create Date: 2022-09-10 22:37:53.665886

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '1f5a89776d38'
down_revision = '32cdd06111c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('RoleData',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rolename', sa.String(length=10), nullable=False),
    sa.Column('rolepic_url', sa.String(length=180), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rolename'),
    sa.UniqueConstraint('rolepic_url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('RoleData')
    # ### end Alembic commands ###
