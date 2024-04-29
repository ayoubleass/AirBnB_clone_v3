#!/usr/bin/python3
"""This script """


from api.v1.views import app_views
from flask import jsonify
from models import storage
import json


@app_views.route("/states/", strict_slashes=False)
def show_states():
    """Return all states objets"""
    result = []
    for state in storage.all("State").items():
        result.append(state[1].to_dict())
    return json.dumps(result, indent=2)


@app_views.route("/states/<state_id>", strict_slashes=False)
def show_state(state_id):
    """Return a specifique State object or raise a 404 error"""
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    return json.dumps(state.to_dict(), indent=2)


@app_views.route("/states/<state_id>", strict_slashes=False)
def delete_state(state_id):
    """Return a specifique State object or raise a 404 error"""
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    storage.delete(status=200)
    return jsonify({},status=200 , indent=2)



@app_views.route("/states", methods=['POST'],strict_slashes=False)
def create_state():
    state = State()
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict())
