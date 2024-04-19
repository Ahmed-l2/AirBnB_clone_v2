#!/usr/bin/python3
"""FLASK APP"""

from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_h1(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    return render_template("6-number_odd_or_even.html", n=n,
                           eo='even' if n % 2 == 0 else 'odd')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
