#!/usr/bin/python3
"""FLASK APP"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pye(text="is_cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<n>", strict_slashes=False)
def num(n):
    return "{} is a number".format(int(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
