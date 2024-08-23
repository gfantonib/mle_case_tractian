from flask import Blueprint, jsonify
import pandas as pd

weights_blueprint = Blueprint("weights", __name__)

csv_file_path = "sensor_data.csv"

@weights_blueprint.route("/<sensor_id>/weights", methods=["GET"])
def sensor_weights(sensor_id):
    try:
        df = pd.read_csv(csv_file_path)
        filtered_df = df[df['sensor_id'] == sensor_id]
        
        if filtered_df.empty:
            return jsonify({"error": f"Sensor ID {sensor_id} not found"}), 404
        
        result_json = filtered_df.to_json(orient='records')
        return result_json
    except Exception as e:
        return jsonify({"error": f"Error retrieving sensor data: {str(e)}"}), 500