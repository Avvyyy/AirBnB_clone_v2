#1/usr/bin/pyhton3
"""Defines routes"""
from flask import Flask
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
    return "Hello HBNB!"

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
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
