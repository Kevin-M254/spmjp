#!/usr/bin/python3
from models import storage
from models.country import Country
from models.league import League
from os import environ
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove current SQLAlchemy Session """
    storage.close()


@app.route('/spmjp_filters', strict_slashes=False)
def spmjp_filters():
    """ SPMJP filters """
    countries = storage.all(Country).values()
    countries = sorted(countries, key=lambda k: k.name)
    ct_lg = []

    for country in countries:
        ct_lg.append([country, sorted(country.leagues, key=lambda k: k.name)])

    return render_template('10-spmjp_filters.html', countries=ct_lg)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
