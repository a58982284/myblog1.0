"""initial migration

Revision ID: 164b9217a1da
Revises: None
Create Date: 2018-03-30 16:33:12.418000

"""

# revision identifiers, used by Alembic.
revision = '164b9217a1da'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spatial_ref_sys')
    op.drop_table('pointcloud_formats')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pointcloud_formats',
    sa.Column('pcid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('schema', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('pcid', name=u'pointcloud_formats_pkey')
    )
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('srid', name=u'spatial_ref_sys_pkey')
    )
    ### end Alembic commands ###
