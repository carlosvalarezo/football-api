import abc
from typing import Any


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, domain_object: Any):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self) -> Any:
        raise NotImplementedError
