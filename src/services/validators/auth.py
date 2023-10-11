from fastapi import HTTPException

from ...repositories.auth import AuthRepository


class AuthValidator:
    def __init__(self) -> None:
        self.auth_repository = AuthRepository()

    async def username_validator(self, username: str):
        res = await self.auth_repository.get_one_by_username(username)
        if res:
            raise HTTPException(detail="User with this username already exists", status_code=409)

    async def email_validator(self, email: str):
        res = await self.auth_repository.get_one_by_email(email)
        if res:
            raise HTTPException(detail="User with this email already exists", status_code=409)

    async def username_email_validators(self, username, email):
        await self.username_validator(username)
        await self.email_validator(email)
