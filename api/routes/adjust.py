from flask import Blueprint, jsonify
import pandas as pd

adjust_blueprint = Blueprint("adjust", __name__)

csv_file_path = "sensor_data.csv"

@adjust_blueprint.route("/<sensor_id>/adjust", methods=["POST"])
def sensor_adjust(sensor_id):
    try:
        df = pd.read_csv(csv_file_path)
        
        if sensor_id not in df['sensor_id'].values:
            return jsonify({"error": f"Sensor ID {sensor_id} not found"}), 404
        
        df.loc[df['sensor_id'] == sensor_id, 'mean'] *= 1.10
        df.to_csv(csv_file_path, index=False)
        
        return jsonify({"message": "Database updated successfully"})
    except Exception as e:
        return jsonify({"error": f"Error adjusting sensor data: {str(e)}"}), 500