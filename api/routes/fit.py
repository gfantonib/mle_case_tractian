from flask import Blueprint, request, jsonify
import numpy as np
import pandas as pd

fit_blueprint = Blueprint("fit", __name__)

parquet_file_path = "sensor_data.parquet"

@fit_blueprint.route("/<sensor_id>/fit", methods=["POST"])
def sensor_fit(sensor_id):
    data = request.get_json()
    values = data.get("values")

    if not isinstance(values, list) or not all(isinstance(x, (int, float)) for x in values):
        return jsonify({"error": "Invalid input: values must be a list of numbers"}), 400
    if len(values) == 0:
        return jsonify({"error": "Empty list of values"}), 400

    try:
        mean = np.mean(values)
        std_dev = np.std(values)
    except Exception as e:
        return jsonify({"error": f"Error calculating statistics: {str(e)}"}), 500

    try:
        df = pd.read_parquet(parquet_file_path)

        new_id = df['id'].max() + 1 if not df.empty else 1

        new_row = pd.DataFrame({'id': [new_id], 'sensor_id': [sensor_id], 'mean': [mean], 'std_dev': [std_dev]})
        df = pd.concat([df, new_row], ignore_index=True)

        df.to_parquet(parquet_file_path, index=False)
        
        result = {
            "id": int(new_id),
            "sensor_id": sensor_id,
            "mean": mean,
            "std_dev": std_dev
        }
        
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Error updating Parquet file: {str(e)}"}), 500