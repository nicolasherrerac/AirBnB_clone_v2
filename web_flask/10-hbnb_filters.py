#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """display html page"""
    return render_template('10-hbnb_filters.html',
                           states=storage.all("State").values(),
                           amenities=storage.all("Amenity").values())


@app.teardown_appcontext
def teardown_func(self):
    """Will excecute after each request
    Closes current sqlalchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)