#!/usr/bin/python3
'''
Start Api
'''
from models import storage
from os import getenv
from flask_cors import CORS
from api.v1.views import app_views
from flask import Flask, make_response, jsonify


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_db(exception):
    """Close Storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """404 Error
    Description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """Main Function"""

    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', '5000'))

    app.run(host=host, port=port, threaded=True)
