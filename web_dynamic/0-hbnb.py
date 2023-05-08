#!/usr/bin/python3
""" Starting FlaskP Web Application """
from models import storage as stg
from models.state import State as St
from models.city import City as Ct
from models.amenity import Amenity as Am
from models.place import Place as Plc
from os import environ as env
from flask import Flask, render_template
import uuid
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    stg.close()


@app.route('/0-hbnb', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    states = stg.all(St).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = stg.all(Am).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = stg.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places, cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
