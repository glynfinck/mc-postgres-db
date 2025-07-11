"""Re-naming column 'author' to 'authors' in provider_content.

Revision ID: 49fa1eedaaa3
Revises: 8b53c8e91507
Create Date: 2025-06-23 22:06:44.657403

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "49fa1eedaaa3"
down_revision: Union[str, Sequence[str], None] = "8b53c8e91507"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("provider_content", "author", new_column_name="authors")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("provider_content", "authors", new_column_name="author")
    # ### end Alembic commands ###
