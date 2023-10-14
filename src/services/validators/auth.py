from typing import NoReturn

from ...repositories.auth import AuthRepository
from .base import BaseValidator


class AuthValidator(BaseValidator):
    def __init__(self) -> None:
        self.auth_repository = AuthRepository()

    async def username_validator(self, username: str) -> None | NoReturn:
        exists = await self.auth_repository.get_one(model_field="username", value=username)
        return await self.already_exists(exists, model_name="user", model_field="username")

    async def email_validator(self, email: str) -> None | NoReturn:
        exists = await self.auth_repository.get_one(model_field="email", value=email)
        return await self.already_exists(exists, model_name="user", model_field="email")

    async def username_email_validators(self, username: str, email: str) -> None:
        await self.username_validator(username)
        await self.email_validator(email)
