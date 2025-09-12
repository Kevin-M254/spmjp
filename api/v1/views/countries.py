#!/usr/bin/python3
""" 
    Objects for handling all default Restful API actions for Countries
"""
from models.country import Country
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
#from flassger.utils import swag_from


@app_views.route('/countries', methods=['GET'], strict_slashes=False)
#@swag_from('documentation/country/get_country.yml', methods=['GET'])
def get_countries():
    """ Retrieves list of all Country objects """
    all_countries = storage.all(Country).values()
    list_countries = []
    for country in all_countries:
        list_countries.append(country.to_dict())
    return jsonify(list_countries)


@app_views.route('/countries/<country_id>', methods=['GET'], strict_slashes=False)
#@swag_from('documentation/country/get_id_country.yml', methods=['GET'])
def get_country(country_id):
    """ Retrieves a specific Country """
    country = storage.get(Country, country_id)
    if not country:
        abort(404)

    return jsonify(country.to_dict())


@app_views.route('/countries/<country_id>', methods=['DELETE'],
                 strict_slashes=False)
#@swag_from('documentation/country/delete_country.yml', methods=['DELETE'])
def delete_country(country_id):
    """ Deletes a Country object """

    country = storage.get(Country, country_id)

    if not country:
        abort(404)

    storage.delete(country)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/countries', methods=['POST'], strict_slashes=False)
#@swag_from('documentation/country/post_country.yml', methods=['POST'])
def post_country():
    """ Creates a Country """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Country(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/countries/<country_id>', methods=['PUT'],
                 strict_slashes=False)
#@swag_from('documentation/country/put_country.yml', methods=['PUT'])
def put_country(country_id):
    """ Updates a Country object """
    country = storage.get(Country, country_id)

    if not country:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(country, key, value)
    storage.save()
    return make_response(jsonify(country.to_dict()), 200)
