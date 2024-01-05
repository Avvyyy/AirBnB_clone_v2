#!/usr/bin/python3
"""Defines routes"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    """
    A home route in flask
    
    Arguments:
    None

    Return:
    Hello HBNB!
    """
    return"Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb route
    
    Arguments:
    None

    Return:
    HBNB
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def returnC(text):
    """
    C route

    Arguments:
    text: Text to be part of the url

    return:
    c + text
    """
    modified_text = text.replace('_', ' ')
    return 'C.{}'.format(modified_text)


if __name__ == "__main__":
    """Making the app to run"""
    app.run(host='0.0.0.0', port=5000)
