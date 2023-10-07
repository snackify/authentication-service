from pydantic import BaseModel, EmailStr


class UserRegistrationRequestSchema(BaseModel):
    username: str
    email: EmailStr
    name: str
    password: str

    # @field_validator('username')
    # def validate_username(cls, username):
    #     if len(username) > 16:
    #         raise HTTPException(status_code=422, detail='Username must be less than 16 characters')
    #     return username
