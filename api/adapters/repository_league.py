import os
import abc
from domain.league import League
import requests


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, league: League):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> League:
        raise NotImplementedError


class APIRepositoryLeague(AbstractRepository):
    def __init__(self,):
        self.uri = os.getenv('FOOTBALL_URI', '')
        self.endpoint = os.getenv('COMPETITIONS_ENDPOINT', '')
        self.api_key = os.getenv('API_KEY_FOOTBALL', '')

    def add(self, league):
        raise NotImplementedError

    def get(self, league):
        uri = f'{self.uri}{self.endpoint}{league}'
        headers = {'X-Auth-Token': self.api_key}
        # print(f'PERRO = {requests.get(uri, headers=headers).json()}')
        return requests.get(uri, headers=headers).json()


class SqlAlchemyRepositoryLeague(AbstractRepository):
    def __init__(self, session):
        self.session = session
        print(f"UNO = {self.session}")

    def add(self, league):
        print(f"DOS = {self.session}, {league}")

        self.session.add(league)

    def get(self, name):
        return self.session.query(League).filter(League.name == name).all()

    def list(self):
        # return self.session.query(League).all()
        return self.session.query(League).count()
