#!/usr/bin/python3
""" flask framework """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ it displays Hello"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run()
