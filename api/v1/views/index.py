#!/usr/bin/python3xx
""" index """

from api.v1.views import app_views
from flask import jsonify
from api.v1.views import app_views


@app_view.route("/status", strict_slashes=False)
def return_status():
    """ return status"""
    return jsonify(status="ok")
