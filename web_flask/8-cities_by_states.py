#!/usr/bin/python3
""" flask framework """
from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ it displays states"""
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_states():
    """ it displays states"""
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    return render_template("8-cities_by_states.html", states=states)



@app.teardown_appcontext
def clean_up(exception):
    """ it cleans the context """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
