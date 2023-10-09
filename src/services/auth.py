from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from src.schemas.auth import UserRegistrationRequestSchema
from src.utils.repository import AbstractRepository


class AuthService:
    def __init__(self, auth_repo: AbstractRepository):
        self.auth_repo = auth_repo()

    async def registration(self, user: UserRegistrationRequestSchema):
        print(user)
        user_dict = user.model_dump()  # todo вынести в репозиторий алхимии

        user_dict["hashed_password"] = user_dict.pop("password")

        try:
            res = await self.auth_repo.add_one(user_dict)
        except IntegrityError:
            raise HTTPException(detail="duplicate", status_code=409)

        return res
