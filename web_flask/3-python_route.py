#!/usr/bin/python3
"""
starts with flask
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """return a message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hi_HBNB():
    """Display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def redirect_parameter(text):
    """Accept parameter"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False, defaults={'text': "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Python is cool"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
