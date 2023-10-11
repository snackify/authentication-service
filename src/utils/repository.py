from abc import ABC, abstractmethod
from typing import NoReturn

from sqlalchemy import select

from ..database.session import async_session


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, *args, **kwargs) -> NoReturn:
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

    async def get_one_by_email(self, email: str):
        async with async_session() as session:
            query = select(self.model).where(self.model.email == email)
            return (await session.execute(query)).scalars().first()

    async def get_one_by_username(self, username: str):
        async with async_session() as session:
            query = select(self.model).where(self.model.username == username)
            return (await session.execute(query)).scalars().first()
