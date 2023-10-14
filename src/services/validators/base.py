from typing import NoReturn

from fastapi import HTTPException

from ...database.models.base import Base


class BaseValidator:
    async def already_exists(self, exists: None | Base, model_name: str, model_field: str) -> None | NoReturn:
        if exists:
            raise HTTPException(
                detail=f"{model_name.title()} with this {model_field.lower()} already exists", status_code=409
            )
        return None
