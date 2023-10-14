from fastapi import Depends

from ..repositories.auth import AuthRepository
from ..repositories.dependencies import get_auth_repository
from ..utils.dependencies import get_hash_password
from ..utils.hash_password import HashPassword
from .auth import AuthService
from .validators.auth import AuthValidator
from .validators.dependencies import get_auth_validator


def get_auth_service(
    auth_repository: AuthRepository = Depends(get_auth_repository),
    hash_password: HashPassword = Depends(get_hash_password),
    auth_validator: AuthValidator = Depends(get_auth_validator),
) -> AuthService:
    return AuthService(
        auth_repository=auth_repository,
        hash_password=hash_password,
        auth_validator=auth_validator,
    )
