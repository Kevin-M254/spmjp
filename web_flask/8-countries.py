#!/usr/bin/python3
from models import storage
from models.country import Country
from os import environ
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove current SQLAlchemy session """
    storage.close()


@app.route('/countries', strict_slashes=False)
@app.route('/countries/<id>', strict_slashes=False)
def countries_country(id=""):
    """ HTML page with a list of countries """
    countries = storage.all(Country).values()
    countries = sorted(countries, key=lambda k: k.name)
    found = 0
    country = ""
    leagues = []

    for i in countries:
        if id == i.id:
            country = i
            found = 1
            break
    if found:
        countries = sorted(country.leagues, key=lambda k: k.name)
        country = country.name

    if id and not found:
        found = 2

    return render_template('8-countries.html', country=country,
                           array=countries, found=found)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
