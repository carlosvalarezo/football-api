import os
from adapters.repository import AbstractRepository
from domain.league import League
import requests


class APIRepositoryLeague(AbstractRepository):
    def __init__(self,):
        self.uri = os.getenv('FOOTBALL_URI', '')
        self.endpoint = os.getenv('COMPETITIONS_ENDPOINT', '')
        self.api_key = os.getenv('API_KEY_FOOTBALL', '')

    def add(self, domain_object):
        raise NotImplementedError

    def get(self, league):
        uri = f'{self.uri}{self.endpoint}{league}'
        headers = {'X-Auth-Token': self.api_key}
        return requests.get(uri, headers=headers).json()


class SqlAlchemyRepositoryLeague(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, league):
        self.session.add(league)
        self.session.flush()
        return league.id

    def get(self, name):
        return self.session.query(League).filter(League.name == name).all()

    def list(self):
        return self.session.query(League).all()
