from fastapi import APIRouter, Depends

from ...services.auth import AuthService
from ...services.dependencies import get_auth_service
from ..schemas.auth import UserRegistrationRequestSchema, UserRegistrationResponseSchema


auth_router = APIRouter(prefix="/v1/auth", tags=["Auth"])


@auth_router.post(path="/registration/", response_model=UserRegistrationResponseSchema)
async def registration(
    request_user: UserRegistrationRequestSchema, auth_service: AuthService = Depends(get_auth_service)
):
    return await auth_service.registration(request_user.model_dump())
