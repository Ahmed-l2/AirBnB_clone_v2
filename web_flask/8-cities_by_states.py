#!/usr/bin/python3
"""FLASK APP"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Closes the db session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    """list of all State objects present in DBStorage sorted by name"""
    states = list(storage.all(State).values())
    states.sort(key=lambda s: s.name)
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states_list():
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
