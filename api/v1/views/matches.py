#!/usr/bin/python3
""" RestFul API actions for Matches """
from models.country import Country
from models.league import League
from models.match import Match
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/leagues/<league_id>/matches', methods=['GET'],
                 strict_slashes=False)
def get_matches(league_id):
    """ Retrieves matches of a particular league """
    league = storage.get(League, league_id)
    if not league:
        abort(404)

    matches = [match.to_dict() for match in league.matches]
    return jsonify(matches)


@app_views.route('/matches', methods=['GET'], strict_slashes=False)
def get_all_matches():
    """ Retrieves all matches """
    all_matches = storage.all(Match).values()
    all_matches = sorted.all(Match, key=lambda k: k.match_id)
    list_matches = []
    for match in all_matches:
        list_matches.append(match.to_dict())
    return jsonify(list_matches)


@app_views.route('/matches/<match_id>', methods=['GET'], strict_slashes=False)
def get_match(match_id):
    """ Retrieves a match based on its id """
    match = storage.get(Match, match_id)
    if not match:
        abort(404)
    return jsonify(match.to_dict())


@app_views.route('/matches/<matches_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_match(match_id):
    """ Deletes a match based on its id """
    match = storage.get(Match, match_id)
    if not match:
        abort(400)
    storage.delete(match)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/leagues/<league_id>/matches', methods=['POST'],
                 strict_slashes=False)
def post_match(league_id):
    """ Creates a Match """
    league = storage.get(League, league_id)
    if not league:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'home_team' not in request.get_json():
        abort(400, description="Home team missing")
    if 'away_team' not in request.get_json():
        abort(400, description="Away team missing")
    if 'h_t_odds' not in request.get_json():
        abort(400, description="Home odds missing")
    if 'x_odds' not in request.get_json():
        abort(400, description="Draw odds missing")
    if 'a_t_odds' not in request.get_json():
        abort(400, description="Away odds missing")

    data['league_id'] = league_id
    instance = Match(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/matches/<match_id>', methods=['PUT'], strict_slashes=False)
def put_match(match_id):
    """ Updates a match """
    match = storage.get(Match, match_id)
    if not match:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    ignore = ['id', 'league_id', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in ingnore:
            setattr(match, key, value)
    storage.save()
    return make_response(jsonify(match.to_dict()), 200)


@app_views.route('/matches_search', methods=['POST'], strict_slashes=False)
def matches_search():
    """ Retrieves all Match objects depending on the JSON in
        the body of the request """
    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data = request.get_json()

    if data and len(data):
        countries = data.get('countries', None)
        leagues = data.get('leagues', None)

    if not data or not len(data) or ( not countries and
                                      not leagues):
        matches = storage.all(Match).values()
        matches = sorted(matches, key=lambda k: k.match_id)
        list_matches = []
        for match in matches:
            list_matches.append(match.to_dict())
        return jsonify(list_matches)

    list_matches = []
    if countries:
        countries_obj = [storage.get(Country, c_id) for c_id in countries]
        for country in countries_obj:
            if country:
                for league in country.leagues:
                    if league:
                        for match in league.matches:
                            list_matches.append(match)

    if leagues:
        league_obj = [storage.get(League, l_id) for l_id in leagues]
        for league in league_obj:
            if league:
                for match in league.matches:
                    if match not in list_matches:
                        list_matches.append(match)

    matches = []
    for m in list_matches:
        d = m.to_dict()
        d.pop('amenities', None)
        matches.append(d)

    return jsonify(matches)
