import os
from adapters.repository import AbstractRepository
from datetime import date
from domain.team import Team
import requests


class APIRepositoryTeam(AbstractRepository):
    def __init__(self,):
        self.uri = os.getenv('FOOTBALL_URI', '')
        self.endpoint = os.getenv('COMPETITIONS_ENDPOINT', '')
        self.api_key = os.getenv('API_KEY_FOOTBALL', '')

    def add(self, team):
        raise NotImplementedError

    def get(self, league):
        uri = f'{self.uri}{self.endpoint}{league}/teams?season={date.today().year}'
        headers = {'X-Auth-Token': self.api_key}
        return requests.get(uri, headers=headers).json()


class SqlAlchemyRepositoryTeam(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, team):
        self.session.add(team)
        self.session.flush()
        return team.id

    def get(self, name):
        return self.session.query(Team).filter(Team.name == name).all()

    def list(self):
        return self.session.query(Team).all()
