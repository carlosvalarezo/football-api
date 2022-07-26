from domain.league import League
from domain.season import Season
from domain.team import Team
from domain.coach import Coach


def test_adds_teams_without_coach_to_league():
    season = Season(starting_date='2022-06-21', ending_date='2022-08-09', current_match='2')
    teams = [Team(name='a_name_A', team_flag='a_team_flag_A', venue='a_venue_A', code='a_code_A'),
             Team(name='a_name_B', team_flag='a_team_flag_B', venue='a_venue_B', code='a_code_B')]
    league_expected = League(name='UEFA Champions League',
                             country='Europe',
                             season=season,
                             code='CL',
                             country_flag='country.svg',
                             league_flag='my_flag.svg')
    for team in teams:
        league_expected.set_teams(team)

    assert len(league_expected.get_teams()) == 2


def test_adds_teams_with_coach_to_league():
    coaches = [Coach(name='A_coach', nationality='A_nationality', code='a_code'),
               Coach(name='B_coach', nationality='B_nationality', code='b_code')]
    season = Season(starting_date='2022-06-21', ending_date='2022-08-09', current_match='2')
    teams = [Team(name='a_name_A', team_flag='a_team_flag_A', venue='a_venue_A', code='a_code_A'),
             Team(name='a_name_B', team_flag='a_team_flag_B', venue='a_venue_B', code='a_code_B')]
    league_expected = League(name='UEFA Champions League',
                             country='Europe',
                             season=season,
                             code='CL',
                             country_flag='country.svg',
                             league_flag='my_flag.svg')
    for team, coach in zip(teams, coaches):
        team.set_coach(coach)
        league_expected.set_teams(team)

    assert len(league_expected.get_teams()) == 2

