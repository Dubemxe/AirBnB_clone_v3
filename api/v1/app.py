#!/usr/bin/python3
'''
Start Api
'''
from models import storage
from api.v1.views import app_views
from flask import Flask
app = Flask(__name__)


app.register_blueprint(app_views)

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()
