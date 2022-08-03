import os

from flask import Flask
from routes.health import health
from routes.setup import setup
from routes.api import api
from adapters.orm import start_mappers

app = Flask(__name__)
start_mappers()
app.register_blueprint(health, url_prefix='/health')
app.register_blueprint(setup, url_prefix='/setup')
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    port = int(os.getenv('APP_PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
