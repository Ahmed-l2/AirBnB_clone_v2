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


@app.route("/states", strict_slashes=False)
def state_list():
    states = storage.all(State)
    return render_template("8-cities_by_states.html",
                           states=storage.all(State))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
