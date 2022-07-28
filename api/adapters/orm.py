from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, mapper

from domain.league import League
from domain.player import Player
from domain.coach import Coach
from domain.team import Team
from domain.league_team import LeagueTeam

import os

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DATABASE_PATH = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(DATABASE_PATH)
get_session = sessionmaker(bind=engine)

metadata = MetaData()


leagues_table = Table(
    "leagues",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=True),
    Column("country", String(100), nullable=True),
    Column("starting_date", Date, nullable=True),
    Column("ending_date", Date, nullable=True),
    Column("current_match", Integer, nullable=True),
    Column("code", String(10), nullable=True),
    Column("country_flag", String(255), nullable=True),
    Column("league_flag", String(255), nullable=True),
)

coaches_table = Table(
    "coaches",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=True),
    Column("nationality", String(255), nullable=True),
    Column("code", String(10), nullable=True)
)

teams_table = Table(
    "teams",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=True),
    Column("venue", String(100), nullable=True),
    Column("code", String(10), nullable=True),
    Column("coach", ForeignKey("coaches.id"), nullable=True),
    Column("team_flag", String(255), nullable=True),
)

league_teams_table = Table(
    "league_teams",
    metadata,
    Column("league", ForeignKey("leagues.id"), primary_key=True, nullable=False, autoincrement=False),
    Column("team", ForeignKey("teams.id"), primary_key=True, nullable=False, autoincrement=False),
)

players_table = Table(
    "players",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=True),
    Column("date_of_birth", Date, nullable=True),
    Column("nationality", String(100), nullable=True),
    Column("position", String(100), nullable=True),
    Column("code", String(10), nullable=True),
    Column("team", ForeignKey("teams.id"), nullable=False)
)


def start_mappers():
    metadata.create_all(engine)
    mapper(League, leagues_table)
    mapper(Team, teams_table)
    mapper(Player, players_table)
    mapper(Coach, coaches_table)
    mapper(LeagueTeam, league_teams_table)
