from flask import Blueprint, jsonify
from services.adjust_service import process_adjust

adjust_blueprint = Blueprint("adjust", __name__)

@adjust_blueprint.route("/<sensor_id>/adjust", methods=["POST"])
def sensor_adjust(sensor_id):
    result = process_adjust(sensor_id)
    return jsonify(result), 200
