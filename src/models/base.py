from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class from which other classes inherit"""

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
