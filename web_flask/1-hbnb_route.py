#!/usr/bin/python3
"""
This module fires up a flask application on the port
0.0.0.0 at port 5000 it ensures strict_slashes is false
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_nbnb():
    """
    basic flask route on default page
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_nbnb_only():
    """
    basic flask route on hbnb
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
