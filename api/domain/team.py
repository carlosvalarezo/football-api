from domain.player import Player
from domain.coach import Coach


class Team:
    def __init__(self,
                 name: str,
                 team_flag: str,
                 venue,
                 code: str):
        self.name = name
        self.team_flag = team_flag
        self.venue = venue
        self.code = code
        self._coach = None
        self._squad = set()

    def set_coach(self, coach: Coach):
        self._coach = coach

    def set_squad(self, squad: Player):
        self._squad = squad
