from adapters.repository import AbstractRepository
from domain.league_team import LeagueTeam


class SqlAlchemyRepositoryLeagueTeam(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, league_team):
        self.session.add(league_team)
        self.session.flush()

    def get(self):
        return self.session.query(LeagueTeam).all()

    def list(self):
        return self.session.query(LeagueTeam).all()
