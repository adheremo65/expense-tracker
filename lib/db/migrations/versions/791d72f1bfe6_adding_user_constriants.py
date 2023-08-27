"""Adding user constriants

Revision ID: 791d72f1bfe6
Revises: b051eb5b3b37
Create Date: 2023-08-27 13:10:52.803678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '791d72f1bfe6'
down_revision: Union[str, None] = 'b051eb5b3b37'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
