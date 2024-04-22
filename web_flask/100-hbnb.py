#!/usr/bin/env python3
"""FLASK APP"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Closes the db session"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb_filters():
    return render_template("100-hbnb.html",
                           states=storage.all(State),
                           amenities=storage.all(Amenity),
                           places=storage.all(Place))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
