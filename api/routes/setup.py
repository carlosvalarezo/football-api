import datetime
import logging
import json

from flask import abort, Blueprint, jsonify, request
from domain.league import League, LeagueCode
from domain.league_team import LeagueTeam
from adapters.repository_league import APIRepositoryLeague, SqlAlchemyRepositoryLeague
from adapters.repository_team import APIRepositoryTeam, SqlAlchemyRepositoryTeam
from adapters.repository_coach import SqlAlchemyRepositoryCoach
from adapters.repository_player import SqlAlchemyRepositoryPlayer
from adapters.repository_league_teams import SqlAlchemyRepositoryLeagueTeam
from exceptions.exceptions import NameAlreadyRegisteredError, NameNotRegisteredError
from adapters.orm import get_session
from service.service import save_data
from mappers.league import LeagueMapper

from mappers.team import TeamMapper

setup = Blueprint('setup', __name__)


@setup.route('league/<string:league_code>/')
def setup_league(league_code):
    try:
        code = LeagueCode(league_code)

        api_league_response = APIRepositoryLeague()
        response_league = api_league_response.get(league=code.code)

        api_teams_response = APIRepositoryTeam()
        response_teams = api_teams_response.get(league=code.code)

        league_mapper = LeagueMapper(response_league)
        league_dt = league_mapper.map_league()

        teams_mapper = TeamMapper(response_teams['teams'])
        teams = teams_mapper.map_teams()

        league_dt.set_teams(teams)
        session = get_session()

        league_repository = SqlAlchemyRepositoryLeague(session=session)
        team_repository = SqlAlchemyRepositoryTeam(session=session)
        coach_repository = SqlAlchemyRepositoryCoach(session=session)
        player_repository = SqlAlchemyRepositoryPlayer(session=session)
        league_team_repository = SqlAlchemyRepositoryLeagueTeam(session=session)

        league_id = save_data(domain_object=league_dt, repo=league_repository, session=session)

        for team in league_dt.get_teams():
            coach_id = save_data(domain_object=team.coach, repo=coach_repository, session=session)
            team.set_coach(coach_id)
            team_id = save_data(domain_object=team, repo=team_repository, session=session)
            league_team = LeagueTeam(league=league_id, team=team_id)
            save_data(domain_object=league_team, repo=league_team_repository, session=session)
            for player in team.squad:
                player.set_team(team_id)
                save_data(domain_object=player, repo=player_repository, session=session)

        return jsonify({'code': league_code})
    except (NameAlreadyRegisteredError,
            NameNotRegisteredError) as error:
        return {'error': error.error,
                'status': error.status_code}