from ..repositories.auth import AuthRepository
from ..utils.hash_password import HashPassword
from .validators.auth import AuthValidator


class AuthService:
    def __init__(self) -> None:
        self.auth_repository = AuthRepository()
        self.hash_password = HashPassword()
        self.auth_validator = AuthValidator()

    async def registration(self, user: dict):
        await self.auth_validator.username_email_validators(username=user["username"], email=user["email"])

        user["hashed_password"] = self.hash_password.create_hash(user.pop("password"))

        res = await self.auth_repository.add_one(user)

        return res
