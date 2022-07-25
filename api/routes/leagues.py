import datetime
import logging
import json

from flask import abort, Blueprint, jsonify, request
from domain.league import League, LeagueCode
from domain.season import Season
from adapters.repository_league import APIRepositoryLeague, SqlAlchemyRepositoryLeague
from database.config import get_session
from service.service import save_league

league_endpoint = Blueprint('setup', __name__)


@league_endpoint.route('league')
def league():
    pass


@league_endpoint.route('import_league/<string:league_code>/')
def league_code_endpoint(league_code):
    code = LeagueCode(league_code)
    api_response = APIRepositoryLeague()
    response = api_response.get(league=code.code)
    print(f"YUPI API = {response}")
    season = Season(starting_date=datetime.datetime.now(), ending_date=datetime.datetime.now(), current_match='2')
    league_dt = League('MY_NAME_TODAY', 'MY_COUNTRY', season, 'MY_CODE', 'MY_COUNTRY_FLAG', 'MY_LEAGUE_FLAG')
    session = get_session()
    league_repository = SqlAlchemyRepositoryLeague(session=session)
    save_league(league=league_dt, repo=league_repository, session=session)
    print(f"YUPI DB = {league_repository.get(name='MY_NAME_TODAY')}")
    return json.dumps({'code': league_code})
