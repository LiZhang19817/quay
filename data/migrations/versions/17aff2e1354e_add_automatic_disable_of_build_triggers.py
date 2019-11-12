"""Add automatic disable of build triggers

Revision ID: 17aff2e1354e
Revises: 61cadbacb9fc
Create Date: 2017-10-18 15:58:03.971526

"""

# revision identifiers, used by Alembic.
revision = '17aff2e1354e'
down_revision = '61cadbacb9fc'

from alembic import op as original_op
from data.migrations.progress import ProgressWrapper
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('repositorybuildtrigger', sa.Column('successive_failure_count', sa.Integer(), server_default='0', nullable=False))
    op.add_column('repositorybuildtrigger', sa.Column('successive_internal_error_count', sa.Integer(), server_default='0', nullable=False))
    # ### end Alembic commands ###

    op.bulk_insert(
        tables.disablereason,
        [
        {'id': 2, 'name': 'successive_build_failures'},
        {'id': 3, 'name': 'successive_build_internal_errors'},
        ],
    )

    # ### population of test data ### #
    tester.populate_column('repositorybuildtrigger', 'successive_failure_count', tester.TestDataType.Integer)
    tester.populate_column('repositorybuildtrigger', 'successive_internal_error_count', tester.TestDataType.Integer)
    # ### end population of test data ### #


def downgrade(tables, tester, progress_reporter):
    op = ProgressWrapper(original_op, progress_reporter)
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('repositorybuildtrigger', 'successive_internal_error_count')
    op.drop_column('repositorybuildtrigger', 'successive_failure_count')
    # ### end Alembic commands ###

    op.execute(tables
                .disablereason
                .delete()
                .where(tables.disablereason.c.name == op.inline_literal('successive_internal_error_count')))

    op.execute(tables
                .disablereason
                .delete()
                .where(tables.disablereason.c.name == op.inline_literal('successive_failure_count')))
