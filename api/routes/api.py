import logging
import json

from flask import abort, Blueprint, jsonify, request
from domain.league import League, LeagueCode
from adapters.repository_league import APIRepositoryLeague, SqlAlchemyRepositoryLeague
from adapters.repository_player import SqlAlchemyRepositoryPlayer
from adapters.orm import get_session
from service.service import save_data, get_data
from exceptions.exceptions import NameAlreadyRegisteredError, NameNotRegisteredError
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)
api = Blueprint('api', __name__)


@dataclass
class PlayerSearch:
    league_code: LeagueCode
    team_code: str


@api.route('league/<string:league_code>/')
def api_league(league_code):
    try:
        PlayerSearch.code = LeagueCode(league_code)
        session = get_session()
        league_repository = SqlAlchemyRepositoryLeague(session=session)

        leagues_sql = get_data(domain_object=PlayerSearch.code, repo=league_repository)

        leagues = [{'name': league.name,
                    'country': league.country,
                    'code': league.code} for league in leagues_sql]

        return jsonify(leagues)
    except NameNotRegisteredError as error:
        return {'error': str(error.error),
                'status': error.status_code}


@api.route('players/<string:league_code>/')
def api_players(league_code):
    try:
        PlayerSearch.league_code = LeagueCode(league_code)
        PlayerSearch.team_code = request.args.get('team', None, type=str)
        session = get_session()
        player_repository = SqlAlchemyRepositoryPlayer(session=session)
        players_sql = get_data(domain_object=PlayerSearch, repo=player_repository)
        players = [{'name': player.player_name,
                    'date_of_birth': player.date_of_birth,
                    'nationality': player.nationality,
                    'position': player.position,
                    'code': player.code,
                    'team': player.team_name,
                    'team_code': player.team_code} for player in players_sql]
        return {'players': players,
                'league': league_code,
                'number_of_players': len(players)}
    except (NameAlreadyRegisteredError,
            NameNotRegisteredError) as error:
        return {'error': str(error.error),
                'status': error.status_code}
