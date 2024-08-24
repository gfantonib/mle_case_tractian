from flask import Blueprint, request, jsonify
import pandas as pd

predict_blueprint = Blueprint("predict", __name__)

parquet_file_path = "sensor_data.parquet"

@predict_blueprint.route("/<sensor_id>/predict", methods=["POST"])
def sensor_predict(sensor_id):
    data = request.get_json()
    discriminator = data.get("values")

    if not isinstance(discriminator, (int, float)):
        return jsonify({"error": "Invalid input: value must be a number"}), 400

    try:
        df = pd.read_parquet(parquet_file_path)
        df_sensor = df[df['sensor_id'] == sensor_id]
        
        if df_sensor.empty:
            return jsonify({"error": f"Sensor ID {sensor_id} not found"}), 404
        
        series_bool = series_bool = 20 >= df_sensor["mean"] + 2*df_sensor["std_dev"]
        return series_bool.to_json()
    except Exception as e:
        return jsonify({"error": f"Error processing prediction: {str(e)}"}), 500