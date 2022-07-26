import datetime
import logging
import json

from flask import abort, Blueprint, jsonify, request
from domain.league import League, LeagueCode
from domain.season import Season
from adapters.repository_league import APIRepositoryLeague, SqlAlchemyRepositoryLeague
from adapters.repository_team import APIRepositoryTeam
from database.config import get_session
from service.service import save_data
from mappers.league import LeagueMapper

league_endpoint = Blueprint('setup', __name__)


@league_endpoint.route('league')
def league():
    pass


@league_endpoint.route('import_league/<string:league_code>/')
def league_code_endpoint(league_code):
    code = LeagueCode(league_code)
    api_league_response = APIRepositoryLeague()
    response_league = api_league_response.get(league=code.code)
    league_mapper = LeagueMapper(response_league)
    league_dt = league_mapper.map_league()
    session = get_session()
    league_repository = SqlAlchemyRepositoryLeague(session=session)
    save_data(domain_object=league_dt, repo=league_repository, session=session)
    return json.dumps({'code': league_code})
