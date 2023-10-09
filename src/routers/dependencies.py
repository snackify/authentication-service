from ..repositories.auth import AuthRepository
from ..services.auth import AuthService


def auth_service():
    return AuthService(AuthRepository)
