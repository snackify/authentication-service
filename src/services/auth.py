from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from ..repositories.auth import AuthRepository
from ..utils.hash_password import HashPassword


class AuthService:
    def __init__(self) -> None:
        self.auth_repository = AuthRepository()
        self.hash_password = HashPassword()
        # self.auth_validator = AuthValidator()

    async def registration(self, user: dict):
        # await self.auth_validator.all_validators(username=user['username'], email=user['email'])

        user["hashed_password"] = self.hash_password.create_hash(user.pop("password"))

        try:
            res = await self.auth_repository.add_one(user)
        except IntegrityError:  # todo выкинуть валидацию в миксин
            raise HTTPException(detail="duplicate email or username", status_code=409)

        return res
