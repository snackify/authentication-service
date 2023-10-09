from ..database.models import User
from ..utils.repository import SQLAlchemyRepository


class AuthRepository(SQLAlchemyRepository):
    model = User
