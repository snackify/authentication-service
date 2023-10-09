from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Loading environments from the .env file"""

    DB_NAME: str = Field(default="authentication")
    DB_USER: str = Field(default="authentication")
    DB_PASS: str = Field(default="authentication")
    DB_PORT: int = Field(default=5432)
    DB_HOST: str = Field(default="db")

    @property
    def SQLALCHEMY_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"


settings = Settings()
