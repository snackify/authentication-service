from ..database.models import User
from .base.sqlalchemy import SQLAlchemyRepository


class AuthRepository(SQLAlchemyRepository):
    model = User
