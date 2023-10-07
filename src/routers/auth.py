from typing import Annotated

from fastapi import APIRouter, Depends

from src.schemas.auth import UserRegistrationRequestSchema

auth_router = APIRouter(prefix='/v1/auth', tags=['Auth'])


# @auth_router.post('/registration/')
# async def registration(
#         user: UserRegistrationRequestSchema,
#         auth_service: Annotated[AuthService, Depends(auth_service)]
# ):
#     pass


@auth_router.get('/test/')
async def test():
    return 'success'
