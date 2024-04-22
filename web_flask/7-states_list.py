#!/usr/bin/python3
""" flask framework """
from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models import state 

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ it displays states"""
    d = storage.all()
    return render_template('7-states_list.html', d=d)


@app.teardown_appcontext
def clean_up():
    """ it cleans the context """
    return strorage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
