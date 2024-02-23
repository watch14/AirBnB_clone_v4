#!/usr/bin/python3xx
""" index """

from models import storage
from api.v1.views import app_views
from flask import jsonify
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status", strict_slashes=False)
def return_status():
    """ return status"""
    return jsonify(status="ok")


@app_views.route("/stats", strict_slashes=False)
def counter():
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
