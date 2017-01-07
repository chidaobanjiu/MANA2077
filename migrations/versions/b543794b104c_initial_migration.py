"""initial migration

Revision ID: b543794b104c
Revises: 51f5ccfba190
Create Date: 2017-01-07 22:36:39.569000

"""

# revision identifiers, used by Alembic.
revision = 'b543794b104c'
down_revision = '51f5ccfba190'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follows')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('follower_id', sa.INTEGER(), nullable=False),
    sa.Column('followed_id', sa.INTEGER(), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], [u'users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], [u'users.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    ### end Alembic commands ###
