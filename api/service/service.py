from adapters.repository import AbstractRepository
from typing import Any


def save_data(domain_object: Any, repo: AbstractRepository, session) -> Any:
    reference = repo.add(domain_object)
    session.commit()
    return reference
