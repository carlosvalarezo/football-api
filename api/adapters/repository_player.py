from adapters.repository import AbstractRepository
from domain.player import Player
from domain.league import League
from domain.team import Team
from domain.league_team import LeagueTeam


class SqlAlchemyRepositoryPlayer(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, player):
        self.session.add(player)
        self.session.flush()
        return player.id

    def get(self, player_search):
        if not player_search.team_code:
            return self.session.query(Player) \
                .with_entities(Team.name.label('team_name'),
                               Team.code.label('team_code'),
                               Player.name.label('player_name'),
                               Player.date_of_birth.label('date_of_birth'),
                               Player.nationality.label('nationality'),
                               Player.position.label('position'),
                               Player.code.label('code')) \
                .filter(League.code == player_search.league_code.code) \
                .filter(Player.team == Team.id) \
                .filter(Team.id == LeagueTeam.team) \
                .filter(League.id == LeagueTeam.league)

        return self.session.query(Player, Team) \
            .with_entities(Team.name.label('team_name'),
                           Team.code.label('team_code'),
                           Player.name.label('player_name'),
                           Player.date_of_birth.label('date_of_birth'),
                           Player.nationality.label('nationality'),
                           Player.position.label('position'),
                           Player.code.label('code')) \
            .filter(League.code == player_search.league_code.code) \
            .filter(Player.team == Team.id) \
            .filter(Team.id == LeagueTeam.team) \
            .filter(Team.code == player_search.team_code) \
            .filter(League.id == LeagueTeam.league)

    def list(self):
        return self.session.query(Player).all()
