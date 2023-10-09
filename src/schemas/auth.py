from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, field_validator


class UserRegistrationRequestSchema(BaseModel):
    """Registration request scheme (DTO)"""

    username: str
    email: EmailStr
    name: str
    password: str

    @field_validator("username")
    def validate_username(cls, username):
        if len(username) > 16:
            raise HTTPException(status_code=422, detail="Username must be less than 16 characters")
        return username


class UserRegistrationResponseSchema(BaseModel):
    """Registration response scheme (DTO)"""

    id: int
    username: str
    email: EmailStr
    name: str
    is_verified: bool
