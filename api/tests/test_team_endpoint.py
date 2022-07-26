import pytest
import requests
from adapters.repository_team import APIRepositoryTeam


class MockResponse:
    @staticmethod
    def json():
        return {
            "competition": {
                "id": 2021,
                "name": "Premier League",
                "code": "PL",
                "type": "LEAGUE",
                "emblem": "https://crests.football-data.org/PL.png"
            },
            "teams": [
                {
                    "id": 57,
                    "name": "Arsenal FC",
                    "shortName": "Arsenal",
                    "tla": "ARS",
                    "crest": "https://crests.football-data.org/57.png",
                    "address": "75 Drayton Park London N5 1BU",
                    "website": "http://www.arsenal.com",
                    "founded": 1886,
                    "clubColors": "Red / White",
                    "venue": "Emirates Stadium",
                    "runningCompetitions": [
                        {
                            "id": 2021,
                            "name": "Premier League",
                            "code": "PL",
                            "type": "LEAGUE",
                            "emblem": "https://crests.football-data.org/PL.png"
                        }
                    ],
                    "coach": {
                        "id": '',
                        "firstName": '',
                        "lastName": '',
                        "name": '',
                        "dateOfBirth": '',
                        "nationality": '',
                        "contract": {
                            "start": '',
                            "until": ''
                        }
                    },
                    "squad": [],
                    "staff": [],
                    "lastUpdated": "2022-02-10T19:48:56Z"
                }]
        }


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
    api_response = APIRepositoryTeam()

    api_result = api_response.get(league="MY_CODE")

    assert api_result["competition"]["name"] == "Premier League"
