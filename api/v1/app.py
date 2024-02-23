#!/usr/bin/python3
""" app """

from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """ Tear It Down To The Ground """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ amar 404 """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST")
    port = os.getenv("HBNB_API_PORT")

    if not host:
        host = "0.0.0.0"
    if not port:
        port = "5000"

    app.run(host=host, port=port, threaded=True)
