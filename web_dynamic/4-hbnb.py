#!/usr/bin/python3
""" Starts a Flask web application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template, request, jsonify
import uuid

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(error):
    """ Remove SQLAlchemy Session """
    storage.close()


@app.route('/4-hbnb/')
def hbnb():
    """ It's alive! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    cache_id = str(uuid.uuid4())

    return render_template('4-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           cache_id=cache_id)


@app.route('/4-hbnb/search', methods=['POST'])
def search_places():
    """ Search for places based on amenities """
    data = request.get_json()
    amenity_ids = data.get('amenities', [])
    places = []

    if amenity_ids:
        places = storage.all(Place).values()
        places = [
                place.to_json() for place in places if all(
                    amenity in place.amenities_id for amenity in amenity_ids
                    )
                ]

    return jsonify(places)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
