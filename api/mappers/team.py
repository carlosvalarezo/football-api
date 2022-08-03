from domain.team import Team
from mappers.coach import CoachMapper
from mappers.player import PlayerMapper


class TeamMapper:
    def __init__(self, teams):
        self.teams = teams
        self.teams_mapped = set()

    def _map_response_to_domain_object(self, team):
        self._set_name(team['name'])
        self._set_team_flag(team['crest'])
        self._set_venue(team['venue'])
        self._set_code(team['id'])
        self._set_squad(team['squad'])
        self._set_coach(team['coach'])

    def _set_squad(self, squad):
        self.squad = set()
        for player in squad:
            player_mapper = PlayerMapper(player)
            player = player_mapper.map_player()
            self.squad.add(player)
        return self.squad

    def _set_name(self, name):
        self.name = name

    def _set_team_flag(self, team_flag):
        self.team_flag = team_flag

    def _set_venue(self, venue):
        self.venue = venue

    def _set_code(self, code):
        self.code = code

    def _map_coach(self, coach):
        coach_mapper = CoachMapper(coach)
        return coach_mapper.map_coach()

    def _set_coach(self, coach):
        self.coach = self._map_coach(coach)

    def map_team(self):
        team = Team(name=self.name,
                    team_flag=self.team_flag,
                    venue=self.venue,
                    code=self.code)
        team.set_squad(self.squad)
        team.set_coach(self.coach)
        return team

    def map_teams(self):
        for team in self.teams:
            self._map_response_to_domain_object(team)
            team_mapped = self.map_team()

            self.teams_mapped.add(team_mapped)
        return self.teams_mapped
