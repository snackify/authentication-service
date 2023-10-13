from typing import NoReturn

from fastapi import HTTPException

from ...repositories.auth import AuthRepository


class AuthValidator:
    def __init__(self) -> None:
        self.auth_repository = AuthRepository()

    async def username_validator(self, username: str) -> None | NoReturn:
        res = await self.auth_repository.get_one(model_field="username", value=username)
        if res:
            raise HTTPException(detail="User with this username already exists", status_code=409)
        return None

    async def email_validator(self, email: str) -> None | NoReturn:
        res = await self.auth_repository.get_one(model_field="email", value=email)
        if res:
            raise HTTPException(detail="User with this email already exists", status_code=409)
        return None

    async def username_email_validators(self, username: str, email: str) -> None:
        await self.username_validator(username)
        await self.email_validator(email)
