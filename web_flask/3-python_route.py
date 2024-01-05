#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def desplay_hbnb():
    return "HBNB"

@app.route("/c/", strict_slashes=False)
@app.route("/c/<text>", strict_slashes=False)
def display_cText(text):
    text = text.replace("_", " ")
    return "C %s" % (text)

@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_pythonText(text="is cool"):
    text = text.replace("_", " ")
    return "Python %s" % (text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
