#!/usr/bin/python3
""" flask framework """
from flask import Flask
from markupsafe import escape
from flask import render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>')
# @app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
def python_text(text=None):
    """ it displays Hello"""
    if text is None:
        return 'Python is cool'
    else:
        text = text.replace('_', ' ')
        return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    """ it displays Hello"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_int(n):
    """ it displays Hello"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
