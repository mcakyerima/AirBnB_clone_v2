#!/usr/bin/python3
"""
This script starts a Flask web app.
- It listens on 0.0.0.0, port 5000.
- Routes:
  - /: Display "Hello HBNB!"
  - /hbnb: Display "HBNB"
  - /c/<text>: Display "C" + text (replace underscores with spaces)
  - /python: Display "Python is cool" (default text is "is cool")
  - /python/<text>: Display "Python" + text (replace underscores with spaces, default is "is cool")
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
    Display a greeting message.
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
    Display "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """
    Display "C" followed by custom text.
    Replace underscores in the text with spaces.
    """
    return "C {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
