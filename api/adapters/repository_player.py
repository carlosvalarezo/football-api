from adapters.repository import AbstractRepository
from domain.player import Player


class SqlAlchemyRepositoryPlayer(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, player):
        self.session.add(player)
        self.session.flush()
        return player.id

    def get(self, name):
        return self.session.query(Player).filter(Player.name == name).all()

    def list(self):
        return self.session.query(Player).all()
