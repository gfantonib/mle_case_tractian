from flask import Blueprint, request, jsonify
from services.fit_service import process_fit

fit_blueprint = Blueprint("fit", __name__)

@fit_blueprint.route("/<sensor_id>/fit", methods=["POST"])
def sensor_fit(sensor_id):
    """
    Endpoint to process fit request for a given sensor ID.

    Args:
        sensor_id (str): The ID of the sensor.
        data (dict): A dictionary containing the values for mean and standard deviation calculations.

    Returns:
        Response: A JSON response containing the result of the fit process with 'id', 'sensor_id', 'mean', and 'std_dev',
                  or an error message with the appropriate status code if the request is invalid or an error occurs.
    """
    result = process_fit(sensor_id, request.get_json())
    status = result.get("status", 200)
    return jsonify(result), status
