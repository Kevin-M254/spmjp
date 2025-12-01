#!/usr/bin/python3
from models import storage
from models.country import Country
from models.league import League
from models.match import Match
from os import environ
from flask import Flask, render_template, request
from posts.blueprint import matches
import uuid


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove current SQLAlchemy Session """
    storage.close()


@app.route('/', strict_slashes=False)
def index():
    """ SPMJP objects """
    countries = storage.all(Country).values()
    countries = sorted(countries, key=lambda k: k.name)
    ct_lg = []

    for country in countries:
        ct_lg.append([country, sorted(country.leagues, key=lambda k: k.name)])

    matches = storage.all(Match).values()
    matches = sorted(matches, key=lambda k: k.match_id)
    per_page = 17
    total_pages = (len(matches) + per_page - 1) // per_page
    page = request.args.get('page', total_pages, type=int)
    start = (page - 1) * per_page
    end = start + per_page
    matches_on_page = matches[start:end]
    return render_template('index.html',
                           countries=ct_lg,
                           cache_id=uuid.uuid4(),
                           matches_on_page=matches_on_page,
                           total_pages=total_pages, page=page)


@app.route('/filters/', strict_slashes=False)
def filters():
    countries = storage.all(Country).values()
    countries = sorted(countries, key=lambda k: k.name)
    ct_lg = []

    for country in countries:
        ct_lg.append([country, sorted(country.leagues, key=lambda k: k.name)])

    matches = storage.all(Match).values()
    matches = sorted(matches, key=lambda k: k.match_id)
    return render_template('main.html', countries=ct_lg,
                           cache_id=str(uuid.uuid4()))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
