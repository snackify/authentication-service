from ..database.models import User
from .base_repositories.sqlalchemy import SQLAlchemyRepository


class AuthRepository(SQLAlchemyRepository):
    model = User
