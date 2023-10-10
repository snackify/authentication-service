from abc import ABC, abstractmethod

from ..database.session import async_session


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self):
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
