from flask import Blueprint, jsonify

health = Blueprint('health', __name__)


@health.route('status')
def health_status():
    return jsonify({'status': 'up'})
