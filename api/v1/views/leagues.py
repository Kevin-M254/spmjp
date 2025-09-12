#!/usr/bin/python3
""" RestFul API actions for leagues """
from models.league import League
from models.country import Country
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/countries/<country_id>/leagues', methods=['GET'], strict_slashes=False)
def get_leagues(country_id):
    """ Retrieves leagues of a specific Country """
    list_leagues = []
    country = storage.get(Country, country_id)
    if not country:
        abort(404)
    for league in country.leagues:
        list_leagues.append(league.to_dict())

    return jsonify(list_leagues)


@app_views.route('/leagues', methods=['GET'], strict_slashes=False)
def get_all_leagues():
    """ Retrieves all leagues """
    all_leagues = storage.all(League).values()
    list_leagues = []
    for league in all_leagues:
        list_leagues.append(league.to_dict())
    return jsonify(list_leagues)


@app_views.route('/leagues/<league_id>', methods=['GET'], strict_slashes=False)
def get_league(league_id):
    """ Retieve specific league based on its id """
    league = storage.get(League, league_id)

    if not league:
        abort(404)
    return jsonify(league.to_dict())


@app_views.route('/leagues/<league_id>', methods=['DELETE'], strict_slashes=False)
def delete_league(league_id):
    """ Deletes a league based on its id """
    league = storage.get(League, league_id)

    if not league:
        abort(404)
    storage.delete(league)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/countries/<country_id>/leagues', methods=['POST'], strict_slashes=False)
def post_league(country_id):
    """ Creates a league based on a Country's id """
    country = storage.get(Country, country_id)
    if not country:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = League(**data)
    instance.country_id = country.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/leagues/<league_id>', methods=['PUT'], strict_slashes=False)
def put_league(league_id):
    """ Updates a League """
    league = storage.get(League, league_id)
    if not league:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'country_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(league, key, value)
    storage.save()
    return make_response(jsonify(league.to_dict()), 200)
