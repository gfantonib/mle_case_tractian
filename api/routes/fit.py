from flask import Blueprint, request, jsonify
import numpy as np
import csv

fit_blueprint = Blueprint("fit", __name__)

csv_file_path = "sensor_data.csv"

@fit_blueprint.route("/<sensor_id>/fit", methods=["POST"])
def sensor_fit(sensor_id):

    data = request.get_json()
    values = data["values"]
    mean = np.mean(values)
    std_dev = np.std(values)
    
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([sensor_id, mean, std_dev])
    
    result = {
        "sensor_id": sensor_id,
        "mean": mean,
        "std_dev": std_dev
    }
    
    return jsonify(result)