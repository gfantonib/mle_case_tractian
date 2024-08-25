from flask import Blueprint, jsonify
from services.adjust_service import process_adjust

adjust_blueprint = Blueprint("adjust", __name__)

@adjust_blueprint.route("/<sensor_id>/adjust", methods=["POST"])
def sensor_adjust(sensor_id):
    """
    Endpoint to adjust the mean value for a given sensor ID.

    Args:
        sensor_id (str): The ID of the sensor.

    Returns:
        Response: A JSON response with a success message if the adjustment is successful,
                  or an error message with the appropriate status code if the sensor ID is not found or an error occurs.
    """
    result = process_adjust(sensor_id)
    status = result.get("status", 200)
    return jsonify(result), status

