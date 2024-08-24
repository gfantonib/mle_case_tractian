from flask import Blueprint, request, jsonify
from services.fit_service import process_fit

fit_blueprint = Blueprint("fit", __name__)

@fit_blueprint.route("/<sensor_id>/fit", methods=["POST"])
def sensor_fit(sensor_id):
    data = request.get_json()
    result = process_fit(sensor_id, data)
    return jsonify(result), 200