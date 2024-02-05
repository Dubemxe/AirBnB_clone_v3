#!/usr/bin/python3
'''
Start Api
'''
from models import storage
from os import getenv
from flask_cors import CORS
from api.v1.views import app_views
from flask import Flask


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_db(exception):
    """Close Storage"""
    storage.close()


if __name__ == "__main__":
    """Main Function"""
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
