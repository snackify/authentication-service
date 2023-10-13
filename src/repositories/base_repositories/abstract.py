from abc import ABC, abstractmethod
from typing import NoReturn


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, *args, **kwargs) -> NoReturn:
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, *args, **kwargs) -> NoReturn:
        raise NotImplementedError
