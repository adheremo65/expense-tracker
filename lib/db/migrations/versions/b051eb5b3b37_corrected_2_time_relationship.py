"""corrected 2 time relationship

Revision ID: b051eb5b3b37
Revises: f717d4d1deaa
Create Date: 2023-08-21 18:19:30.148164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b051eb5b3b37'
down_revision: Union[str, None] = 'f717d4d1deaa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###