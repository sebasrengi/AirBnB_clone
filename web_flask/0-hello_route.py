#!/usr/bin/python3
"""Write a script that start a FlaskWeb application """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def task_0():
    """ Task 0 Function """
    return("Hello HBNB!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
