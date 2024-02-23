#!/usr/bin/python3xx
""" index """

import models
from models import storage
from models.base_model import BaseModel
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", strict_slashes=False)
def return_status():
    """ return status"""
    return jsonify(status="ok")


@app_views.route("/stats", strict_slashes=False)
def counter(self):
    """ counter """
    all_c = {
                "amenities": Amenity,
                "cities": City,
                "places": Place,
                "reviews": Review,
                "states": State,
                "users": User
            }

    for key in all_c:
        all_c[key] = storage.count(all_c[key])

    return jsonify(all_c)
