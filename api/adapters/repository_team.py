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

