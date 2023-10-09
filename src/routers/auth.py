from typing import Annotated

from fastapi import APIRouter, Depends

from ..schemas.auth import UserRegistrationRequestSchema
from ..services.auth import AuthService
from .dependencies import auth_service


auth_router = APIRouter(prefix="/v1/auth", tags=["Auth"])


@auth_router.post("/registration/")  # , response_model=UserRegistrationResponseSchema)
async def registration(
    request_user: UserRegistrationRequestSchema,
    local_auth_service: Annotated[AuthService, Depends(auth_service)],
):
    user = await local_auth_service.registration(request_user)
    return user
