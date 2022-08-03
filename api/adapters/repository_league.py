import http
import os
from adapters.repository import AbstractRepository
from domain.league import League
from exceptions.exceptions import NameAlreadyRegisteredError, NameNotRegisteredError
import requests
from sqlalchemy.exc import IntegrityError


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
        try:
            self.session.add(league)
            self.session.flush()
            return league.id
        except IntegrityError as e:
            raise NameAlreadyRegisteredError(e.orig.diag.message_detail, http.HTTPStatus.BAD_REQUEST)

    def get(self, league_code=None):
        league = self.session.query(League).filter(League.code == league_code.code)
        if league.count() == 0:
            raise NameNotRegisteredError('Name not registered', http.HTTPStatus.BAD_REQUEST)
        return league

    def list(self):
        return self.session.query(League).all()
