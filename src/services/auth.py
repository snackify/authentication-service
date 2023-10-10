from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from ..repositories.auth import AuthRepository
from ..schemas.auth import UserRegistrationRequestSchema
from ..utils.hash_password import HashPassword


class AuthService(AuthRepository, HashPassword):
    async def registration(self, user: UserRegistrationRequestSchema):
        user_dict = user.model_dump()  # todo вынести отсюда этот dump

        user_dict["hashed_password"] = self.create_hash(user_dict.pop("password"))

        try:
            res = await self.add_one(user_dict)
        except IntegrityError:
            raise HTTPException(detail="duplicate email or username", status_code=409)

        return res
