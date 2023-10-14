from .auth import AuthValidator


async def get_auth_validator() -> AuthValidator:
    return AuthValidator()
