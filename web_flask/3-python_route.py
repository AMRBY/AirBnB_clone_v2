#!/usr/bin/python3
""" flask framework """
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ it displays Hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ it displays Hello"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ it displays Hello"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
def python_text(text):
    """ it displays Hello"""
    text = text.replace('_', ' ')
    return f'python {escape(text)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
