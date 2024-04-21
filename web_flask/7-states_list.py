#!/usr/bin/python3
""" flask framework """
from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ it displays states"""
    d = storage.all()
    return render_template('7-states_list.html', d=d)


@app.teardown_appcontext
def clean_up():
    """ it cleans the context """
    return storage.close()


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ it displays Hello"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def template_odd_even(n):
    """ it displays Hello"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
