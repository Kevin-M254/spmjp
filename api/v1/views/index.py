#!/usr/bin/python3
""" Index """
from models.country import Country
from models.league import League
from models.user import User
from models.match import Match
from models.prediction import Prediction
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Country, League, User, Match, Prediction]
    names = ["countries", "leagues", "users", "matches", "predictions"]

    objs = {}
    for i in range(len(classes)):
        objs[names[i]] = storage.count(classes[i])

    return jsonify(objs)
