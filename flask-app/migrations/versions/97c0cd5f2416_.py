"""empty message

Revision ID: 97c0cd5f2416
Revises: 
Create Date: 2022-09-28 10:36:13.085470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97c0cd5f2416'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aluno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('nascimennto', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('autor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('nascimento', sa.Date(), nullable=False),
    sa.Column('post', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.Text(), nullable=False),
    sa.Column('autor_id', sa.Integer(), nullable=False),
    sa.Column('conteudo', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['autor_id'], ['autor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('autor')
    op.drop_table('aluno')
    # ### end Alembic commands ###