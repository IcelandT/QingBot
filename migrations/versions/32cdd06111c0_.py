"""empty message

Revision ID: 32cdd06111c0
Revises: dc8d45531895
Create Date: 2022-09-10 22:37:06.833642

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '32cdd06111c0'
down_revision = 'dc8d45531895'
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
    op.drop_index('rolename', table_name='roledata')
    op.drop_index('rolepic_url', table_name='roledata')
    op.drop_table('roledata')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roledata',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('rolename', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('rolepic_url', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('rolepic_url', 'roledata', ['rolepic_url'], unique=False)
    op.create_index('rolename', 'roledata', ['rolename'], unique=False)
    op.drop_table('RoleData')
    # ### end Alembic commands ###
