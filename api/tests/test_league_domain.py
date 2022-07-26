from mappers.league import LeagueMapper
from domain.league import League
from domain.season import Season


def test_maps_league_api_response_to_league_model_no_teams():
    payload = {'area': {'id': 2077,'name': 'Europe', 'code': 'EUR', 'flag': 'country_flag.svg'},
               'id': 2001, 'name': 'UEFA Champions League', 'code': 'CL', 'type': 'CUP',
               'emblem': 'league_flag',
               'currentSeason': {'id': 1491,
                                 'startDate': '2022-06-21',
                                 'endDate': '2022-08-09',
                                 'currentMatchday': 2,
                                 'winner': None}}
    season = Season(starting_date='2022-06-21', ending_date='2022-08-09', current_match='2')
    expected = League(name='UEFA Champions League',
                      country='Europe',
                      season=season,
                      code='CL',
                      country_flag='country.svg',
                      league_flag='my_flag.svg')
    league_mapper = LeagueMapper(payload)

    league_mapped = league_mapper.map_league()

    assert league_mapped == expected
