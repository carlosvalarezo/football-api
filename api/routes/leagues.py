from flask import abort, Blueprint, jsonify, request
from models.models import League

league_endpoint = Blueprint('setup', __name__)


@league_endpoint.route('league')
def league():
    _league = League(league_name="MY_LEAGUE", league_country="MY_COUNTRY")
    _league.insert()
    return jsonify({'status': _league.league_id})



