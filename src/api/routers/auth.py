from fastapi import APIRouter, Depends

from src.api.dependencies import get_auth_service
from src.api.schemas.auth import UserRegistrationRequestSchema, UserRegistrationResponseSchema
from src.services.auth import AuthService


auth_router = APIRouter(prefix="/v1/auth", tags=["Auth"])


@auth_router.post(path="/registration/", response_model=UserRegistrationResponseSchema)
async def registration(
    request_user: UserRegistrationRequestSchema, auth_service: AuthService = Depends(get_auth_service)
):
    return await auth_service.registration(request_user.model_dump())
