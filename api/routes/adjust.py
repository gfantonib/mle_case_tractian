from flask import Blueprint, jsonify
import pandas as pd

adjust_blueprint = Blueprint("adjust", __name__)

parquet_file_path = "sensor_data.parquet"

@adjust_blueprint.route("/<sensor_id>/adjust", methods=["POST"])
def sensor_adjust(sensor_id):
    try:
        df = pd.read_parquet(parquet_file_path)
        
        if sensor_id not in df['sensor_id'].values:
            return jsonify({"error": f"Sensor ID {sensor_id} not found"}), 404
        
        df.loc[df['sensor_id'] == sensor_id, 'mean'] *= 1.10
        df.to_parquet(parquet_file_path, index=False)
        
        return jsonify({"message": "Database updated successfully"})
    except Exception as e:
        return jsonify({"error": f"Error adjusting sensor data: {str(e)}"}), 500