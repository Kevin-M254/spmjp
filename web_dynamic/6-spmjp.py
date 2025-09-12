#!/usr/bin/python3
from models import storage
from models.country import Country
from models.league import League
from models.match import Match
from os import environ
from flask import Flask, render_template
import uuid
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove current SQLAlchemy Session """
    storage.close()


@app.route('/6-spmjp/', strict_slashes=False)
def spmjp_filters():
    """ SPMJP objects """
    countries = storage.all(Country).values()
    countries = sorted(countries, key=lambda k: k.name)
    ct_lg = []

    for country in countries:
        ct_lg.append([country, sorted(country.leagues, key=lambda k: k.name)])

    matches = storage.all(Match).values()
    matches = sorted(matches, key=lambda k: k.match_id)
    return render_template('100-spmjp.html',
                           countries=ct_lg,
                           matches=matches, cache_id=uuid.uuid4())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
