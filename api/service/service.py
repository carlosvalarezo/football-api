import os
from domain.league import League
from adapters.repository_league import AbstractRepository


def load_endpoint_env_vars():
    return os.getenv('FOOTBALL_URI'), os.getenv('COMPETITIONS_ENDPOINT')


def save_league(league: League, repo: AbstractRepository, session) -> str:
    repo.add(league=league)
    # print(f"YUPI DB = {repo.get(name='MY_NAME_TODAY')}")
    session.commit()

# def add_team_to_league(league: League, team: Team, data: dict):
#     pass

