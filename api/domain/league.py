from dataclasses import dataclass
from domain.team import Team
from domain.season import Season


@dataclass(frozen=True)
class LeagueCode:
    code: str


class League:
    def __init__(self,
                 name: str,
                 country: str,
                 season: Season,
                 code: str,
                 country_flag: str,
                 league_flag: str):
        self.name = name
        self.country = country
        self.starting_date = season.starting_date
        self.ending_date = season.ending_date
        self.current_match = season.current_match
        self.code = code
        self.country_flag = country_flag
        self.league_flag = league_flag
        self._teams = set()

    def __eq__(self, other):
        if not isinstance(other, League):
            return False
        return other.code == self.code

    def set_teams(self, team: Team):
        self._teams.add(team)

    def get_teams(self):
        return self._teams
