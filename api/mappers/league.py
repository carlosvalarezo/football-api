from domain.season import Season
from domain.league import League


class LeagueMapper:
    def __init__(self, data):
        self._set_name(data)
        self._set_country(data)
        self._set_season(data)
        self._set_code(data)
        self._set_country_flag(data)
        self._set_league_flag(data)

    def _set_name(self, data):
        self.name = data['name']

    def _set_country(self, data):
        self.country = data['area']['name']

    def _set_season(self, data):
        starting_date = data['currentSeason']['startDate']
        ending_date = data['currentSeason']['endDate']
        current_match = data['currentSeason']['currentMatchday']
        self.season = Season(starting_date, ending_date, current_match)

    def _set_code(self, data):
        self.code = data['code']

    def _set_country_flag(self, data):
        self.country_flag = data['area']['flag']

    def _set_league_flag(self, data):
        self.league_flag = data['emblem']

    def map_league(self):
        return League(name=self.name,
                      country=self.country,
                      season=self.season,
                      code=self.code,
                      country_flag=self.country_flag,
                      league_flag=self.league_flag)
