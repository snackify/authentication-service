from .auth import AuthRepository


async def get_auth_repository():
    return AuthRepository()
