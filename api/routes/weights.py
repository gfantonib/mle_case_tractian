from flask import Blueprint, jsonify
from services.weights_service import get_weights

weights_blueprint = Blueprint("weights", __name__)

@weights_blueprint.route("/<sensor_id>/weights", methods=["GET"])
def sensor_weights(sensor_id):
    result = get_weights(sensor_id)
    return jsonify(result), result.get("status", 200)
