from flask import Blueprint
import pandas as pd

adjust_blueprint = Blueprint("adjust", __name__)

csv_file_path = "sensor_data.csv"

@adjust_blueprint.route("/<sensor_id>/adjust", methods=["POST"])
def sensor_adjust(sensor_id):
    
	df = pd.read_csv(csv_file_path)	
	df.loc[df['sensor_id'] == sensor_id, ['mean']] *= 1.10
	df.to_csv(csv_file_path, index=False)

	return {"values": "DataBase updated!"}