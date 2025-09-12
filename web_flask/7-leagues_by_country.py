#!/usr/bin/python3
from models import storage
from models.country import Country
#from models.league import League
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove current SQLAlchemy session """
    storage.close()


@app.route('/countries_list', strict_slashes=False)
def countries_list():
    """ HTML page with a list of countries """
    countries = storage.all(Country).values()
    countries = sorted(countries, key=lambda k: k.name)
    return render_template('6-countries_list.html', countries=countries)


@app.route('/leagues_by_country', strict_slashes=False)
def leagues_list():
    """ HTML page with a list of leagues """
    countries = storage.all(Country).values()
    countries = sorted(countries, key=lambda k: k.name)
    ct_lg = []
    for country in countries:
        ct_lg.append([country, sorted(country.leagues, key=lambda k: k.name)])
    return render_template('7-leagues_by_country.html',
                           countries=ct_lg, h_1="Countries")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
