from adapters.repository import AbstractRepository
from domain.coach import Coach


class SqlAlchemyRepositoryCoach(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, coach):
        self.session.add(coach)
        self.session.flush()
        return coach.id

    def get(self):
        return self.session.query(Coach).all()

    def list(self):
        return self.session.query(Coach).all()
