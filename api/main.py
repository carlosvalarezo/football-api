import os

from flask import Flask
from routes.health import health_endpoint
from routes.leagues import league_endpoint
from models.database import setup_db

app = Flask(__name__)
app.register_blueprint(health_endpoint, url_prefix='/api')
app.register_blueprint(league_endpoint, url_prefix='/setup')
setup_db(app)

if __name__ == '__main__':
    port = int(os.getenv('APP_PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
