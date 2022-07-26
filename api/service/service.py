from adapters.repository import AbstractRepository
from typing import Any


def save_data(domain_object: Any, repo: AbstractRepository, session):
    repo.add(domain_object)
    session.commit()
