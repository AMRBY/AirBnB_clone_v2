#!/usr/bin/python3
""" flask framework """
from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<ids>", strict_slashes=False)
def states_id(ids=None):
    """ it displays states"""
    states = list(storage.all(State).values())
    if ids is None:
        states.sort(key=lambda x: x.name)
        return render_template("9-states.html", states=states, cities=None)
    else:
        for state in states:
            if state.id == ids:
                state.cities.sort(key=lambda x: x.name)
                return render_template(
                        "9-states.html", cities=state.cities,
                        name=state.name, yes=1)
        return render_template("9-states.html", cities='something', yes=0)


@app.teardown_appcontext
def clean_up(exception):
    """ it cleans the context """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
