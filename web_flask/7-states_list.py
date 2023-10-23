#!/usr/bin/python3
"""
simple Flask app to connect to db and construct page
"""
from flask import Flask, render_template

from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def all_cities_by_states():
    """
    construct cities by states
    """
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)
    for state in all_states:
        state.cities.sort(key=lambda x: x.name)
    for_page = {
            'states': all_states
    }
    return render_template('7-states_list.html', **for_page)


@app.teardown_appcontext
def flask_teardown(exc):
    """teardown, close database connection"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
