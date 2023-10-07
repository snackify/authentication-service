from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base model with id"""

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
