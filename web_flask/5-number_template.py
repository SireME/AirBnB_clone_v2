#!/usr/bin/python3
"""
This module fires up a flask application on the port
0.0.0.0 at port 5000 it ensures strict_slashes is false
"""
from flask import Flask, render_template


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


@app.route("/c/<text>")
def url_mapping(text):
    """
    manipulate urls
    """
    my_text = text.replace("_", " ")
    return f"C {my_text}"


@app.route("/python/<text>")
@app.route("/python", defaults={"text": "is cool"})
def url_mapping_with_default(text):
    """
    route url with default value
    """
    my_text = text.replace("_", " ")
    return f"Python {my_text}"


@app.route("/number/<int:n>")
def url_routing_integer(n):
    """
    route url ending as integer
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def template_number(n):
    """
    serve flask template base on number url
    """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
