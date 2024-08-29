from flask import Blueprint, request, jsonify
from services.predict_service import process_predict

predict_blueprint = Blueprint("predict", __name__)

@predict_blueprint.route("/<sensor_id>/predict", methods=["POST"])
def sensor_predict(sensor_id):
    """
    Endpoint to process prediction request for a given sensor ID.

    Args:
        sensor_id (str): The ID of the sensor.
        data (dict): A dictionary containing the discriminator value for the prediction.

    Returns:
        Response: A JSON response containing the prediction results,
                  or an error message with the appropriate status code if the request is invalid or an error occurs.
    """
    result = process_predict(sensor_id, request.get_json())
    status = result.get("status", 200)
    return jsonify(result), status
