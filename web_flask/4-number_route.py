#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """function that return a text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function that print hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """function thar print C is fun"""
    string = text.replace("_", " ")
    return 'C {}'.format(string)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """function that print C is fun"""
    string = text.replace("_", " ")
    return 'Python {}'.format(string)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """function that display a integer"""
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
