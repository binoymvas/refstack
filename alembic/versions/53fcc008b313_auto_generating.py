"""auto generating

Revision ID: 53fcc008b313
Revises: 501f41fac63a
Create Date: 2013-09-20 10:30:23.782772

"""

# revision identifiers, used by Alembic.
revision = '53fcc008b313'
down_revision = '501f41fac63a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cloud_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cloud_id'], ['cloud.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('test_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('blob', sa.Binary(), nullable=True),
    sa.ForeignKeyConstraint(['test_id'], ['test.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('test_id', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(length=1024), nullable=True),
    sa.Column('finished', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['test_id'], ['test.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    
    op.add_column(u'user', sa.Column('vendor_id', sa.Integer(), nullable=True))
    op.add_column(u'user', sa.Column('authorized', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'user', 'authorized')
    op.drop_column(u'user', 'vendor_id')
    op.add_column(u'cloud', sa.Column(u'vendor_id', sa.INTEGER(), nullable=True))
    op.drop_table('test_status')
    op.drop_table('test_results')
    op.drop_table('test')
    ### end Alembic commands ###
