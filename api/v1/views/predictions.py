#!/usr/bin/python3
""" RestFul API actions for predictions """
from models.prediction import Prediction
from models.user import User
from models.match import Match
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/matches/<match_id>/predictions', methods=['GET'], strict_slashes=False)
def get_predictions(match_id):
    """ Retrieves predictions of a Match """
    match = storage.get(Match, match_id)
    if not match:
        abort(404)
    predictions = [prediction.to_dict() for prediction in match.predictions]
    return jsonify(predictions)


@app_views.route('/predictions', methods=['GET'],
                 strict_slashes=False)
def get_all_predictions():
    all_preds = storage.all(Prediction).values()
    list_preds = []

    for prediction in all_preds:
        list_preds.append(prediction.to_dict())
    return jsonify(list_preds)


@app_views.route('/predictions/<prediction_id>', methods=['GET'], strict_slashes=False)
def get_prediction(prediction_id):
    """ Retrieves a Prediction object """
    prediction = storage.get(Prediction, prediction_id)
    if not prediction:
        abort(404)
    return jsonify(prediction.to_dict())


@app_views.route('/predictions/<prediction_id>', methods=['DELETE'], strict_slashes=False)
def delete_prediction(prediction_id):
    """ Deletes a Prediction object """
    pred = storage.get(Prediction, prediction_id)
    if not pred:
        abort(404)
    storage.delete(pred)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/matches/<match_id>/predictions', methods=['POST'], strict_slashes=False)
def post_pred(match_id):
    """ Creates a Prediction object """
    match = storage.get(Match, match_id)
    if not match:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")

    data = request.get_json()
    user = storage.get(User, data['user_id'])
    if not user:
        abort(400)
    if 'prediction' not in request.get_json():
        abort(400, description="Prediction is missing")
    data['match_id'] = match_id
    instance = Prediction(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 200)


@app_views.route('/predictions/<prediction_id>', methods=['PUT'], strict_slashes=False)
def put_prediction(prediction_id):
    """ Updates a Prediction """
    pred = storage.get(Prediction, prediction_id)
    if not pred:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'user_id', 'match_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(pred, key, value)
    storage.save()
    return make_response(jsonify(pred.to_dict()), 200)
