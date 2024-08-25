from flask import Blueprint, jsonify
from services.weights_service import get_weights

weights_blueprint = Blueprint("weights", __name__)

@weights_blueprint.route("/<sensor_id>/weights", methods=["GET"])
def sensor_weights(sensor_id):
    """
    Endpoint to retrieve weights for a given sensor ID.

    Args:
        sensor_id (str): The ID of the sensor.

    Returns:
        Response: A JSON response containing the weights of the sensor,
                  or an error message with the appropriate status code if the sensor ID is not found or an error occurs.
    """
    result = get_weights(sensor_id)
    status = result.get("status", 200)
    return jsonify(result), status
