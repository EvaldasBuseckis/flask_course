"""first migration

Revision ID: 975812041921
Revises: 
Create Date: 2022-07-28 20:30:25.859175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '975812041921'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('phone', sa.String(length=40), nullable=True))
    op.create_unique_constraint(None, 'messages', ['phone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'messages', type_='unique')
    op.drop_column('messages', 'phone')
    # ### end Alembic commands ###