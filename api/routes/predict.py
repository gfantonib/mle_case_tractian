from flask import Blueprint, request, jsonify
from services.predict_service import process_predict

predict_blueprint = Blueprint("predict", __name__)

@predict_blueprint.route("/<sensor_id>/predict", methods=["POST"])
def sensor_predict(sensor_id):
    data = request.get_json()
    result = process_predict(sensor_id, data)
    return jsonify(result), result.get("status", 200)
