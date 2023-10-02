from sqlalchemy import Column, Boolean, String

from .base import Base


class User(Base):
    __tablename__ = 'users'

    username = Column(String(16), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    name = Column(String(32))
    hashed_password = Column(String(64), nullable=False)
    is_verified = Column(Boolean, nullable=False, default=False)
