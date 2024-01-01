#!/usr/bin/python3
"""
This Script Starts a Flask App and listens on 0.0.0.0,
	Listens on port 5000.
	Home route /: displays "Hello HBNB!"
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
