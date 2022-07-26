import pytest
import requests
from adapters.repository_league import APIRepositoryLeague, SqlAlchemyRepositoryLeague


class MockResponse:
    @staticmethod
    def json():
        return {'area':
                    {'id': 2077,
                     'name': 'Europe',
                     'code': 'EUR',
                     'flag': 'https://crests.football-data.org/EUR.svg'},
                'id': 2001,
                'name': 'My_Champions_League',
                'code': 'MY_CODE',
                'type': 'CUP',
                'emblem': 'https://crests.football-data.org/CL.png',
                'currentSeason':
                    {'id': 1491,
                     'startDate': '2022-06-21',
                     'endDate': '2022-07-27',
                     'currentMatchday': 2,
                     'winner': None}}


@pytest.fixture
def mock_get_request(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


@pytest.fixture
def mock_endpoint(monkeypatch):
    monkeypatch.setenv("COMPETITIONS_ENDPOINT", "/my/endpoint")


@pytest.fixture
def mock_uri(monkeypatch):
    monkeypatch.setenv("FOOTBALL_URI", "https://mygreaturi.com")


def test_it_should_receive_response_from_football_api(mock_get_request, mock_endpoint, mock_uri):
    api_response = APIRepositoryLeague()

    api_result = api_response.get(league="MY_CODE")

    assert api_result["name"] == "My_Champions_League"

