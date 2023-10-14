from ..api.schemas.auth import UserRegistrationResponseSchema
from ..repositories.auth import AuthRepository
from ..utils.hash_password import HashPassword
from .validators.auth import AuthValidator


class AuthService:
    def __init__(
        self, auth_repository: AuthRepository, hash_password: HashPassword, auth_validator: AuthValidator
    ) -> None:
        self.auth_repository = auth_repository
        self.hash_password = hash_password
        self.auth_validator = auth_validator

    async def registration(self, user: dict) -> UserRegistrationResponseSchema:
        await self.auth_validator.username_email_validators(username=user["username"], email=user["email"])

        user["hashed_password"] = self.hash_password.create_hash(user.pop("password"))

        res = await self.auth_repository.add_one(user)

        return res
