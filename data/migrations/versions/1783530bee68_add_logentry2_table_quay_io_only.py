"""Add LogEntry2 table - QUAY.IO ONLY

Revision ID: 1783530bee68
Revises: 5b7503aada1b
Create Date: 2018-05-17 16:32:28.532264

"""

# revision identifiers, used by Alembic.
revision = '1783530bee68'
down_revision = '5b7503aada1b'

from alembic import op as original_op
from data.migrations.progress import ProgressWrapper
import sqlalchemy as sa


def upgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logentry2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kind_id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('performer_id', sa.Integer(), nullable=True),
    sa.Column('repository_id', sa.Integer(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.Column('ip', sa.String(length=255), nullable=True),
    sa.Column('metadata_json', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['kind_id'], ['logentrykind.id'], name=op.f('fk_logentry2_kind_id_logentrykind')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_logentry2'))
    )
    op.create_index('logentry2_account_id', 'logentry2', ['account_id'], unique=False)
    op.create_index('logentry2_account_id_datetime', 'logentry2', ['account_id', 'datetime'], unique=False)
    op.create_index('logentry2_datetime', 'logentry2', ['datetime'], unique=False)
    op.create_index('logentry2_kind_id', 'logentry2', ['kind_id'], unique=False)
    op.create_index('logentry2_performer_id', 'logentry2', ['performer_id'], unique=False)
    op.create_index('logentry2_performer_id_datetime', 'logentry2', ['performer_id', 'datetime'], unique=False)
    op.create_index('logentry2_repository_id', 'logentry2', ['repository_id'], unique=False)
    op.create_index('logentry2_repository_id_datetime', 'logentry2', ['repository_id', 'datetime'], unique=False)
    op.create_index('logentry2_repository_id_datetime_kind_id', 'logentry2', ['repository_id', 'datetime', 'kind_id'], unique=False)
    # ### end Alembic commands ###


def downgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('logentry2')
    # ### end Alembic commands ###
