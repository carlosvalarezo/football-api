import os

from flask import Flask
from routes.health import health_endpoint

app = Flask(__name__)
app.register_blueprint(health_endpoint, url_prefix='/api')

if __name__ == '__main__':
    port = int(os.getenv('APP_PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
