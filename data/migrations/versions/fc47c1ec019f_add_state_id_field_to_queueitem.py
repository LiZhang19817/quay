"""Add state_id field to QueueItem

Revision ID: fc47c1ec019f
Revises: f5167870dd66
Create Date: 2017-01-12 15:44:23.643016

"""

# revision identifiers, used by Alembic.
revision = 'fc47c1ec019f'
down_revision = 'f5167870dd66'

from alembic import op as original_op
from data.migrations.progress import ProgressWrapper
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('queueitem', sa.Column('state_id', sa.String(length=255), nullable=False, server_default=''))
    op.create_index('queueitem_state_id', 'queueitem', ['state_id'], unique=False)
    # ### end Alembic commands ###

    # ### population of test data ### #
    tester.populate_column('queueitem', 'state_id', tester.TestDataType.String)
    # ### end population of test data ### #


def downgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('queueitem_state_id', table_name='queueitem')
    op.drop_column('queueitem', 'state_id')
    # ### end Alembic commands ###
