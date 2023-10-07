from abc import ABC


class AbstractRepository(ABC):
    pass


class SQLAlchemyRepository(AbstractRepository):
    model = None
