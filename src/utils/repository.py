from abc import ABC, abstractmethod
from typing import NoReturn

from sqlalchemy import select

from ..database.session import async_session


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, *args, **kwargs) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, *args, **kwargs) -> NoReturn:
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict):
        async with async_session() as session:
            model_obj = self.model()
            for k, v in data.items():
                setattr(model_obj, k, v)
            session.add(model_obj)
            await session.commit()

            return model_obj

    async def get_one(self, model_field: str, value: str):
        async with async_session() as session:
            field = getattr(self.model, model_field)
            query = select(self.model).where(field == value)
            return (await session.execute(query)).scalars().first()
