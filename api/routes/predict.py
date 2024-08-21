from flask import Blueprint, request
import pandas as pd

predict_blueprint = Blueprint("predict", __name__)

csv_file_path = "sensor_data.csv"

@predict_blueprint.route("/<sensor_id>/predict", methods=["POST"])
def sensor_predict(sensor_id):

	data = request.get_json()
	discriminator = data["values"]

	df = pd.read_csv(csv_file_path)
	df_sensor = df[df['sensor_id'] == sensor_id]

	series_bool = discriminator >= df_sensor["mean"] + 2*df_sensor["std_dev"]

	return series_bool.to_json()