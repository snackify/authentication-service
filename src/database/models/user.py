from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(type_=String(16), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(type_=String(32))
    hashed_password: Mapped[str] = mapped_column(type_=String(64), nullable=False)
    is_verified: Mapped[bool] = mapped_column(nullable=False, default=False)
