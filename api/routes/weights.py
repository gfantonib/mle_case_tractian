from flask import Blueprint
import pandas as pd

weights_blueprint = Blueprint("weights", __name__)

csv_file_path = "sensor_data.csv"

@weights_blueprint.route("/<sensor_id>/weights", methods=["GET"])
def sensor_weights(sensor_id):

    df = pd.read_csv(csv_file_path)
    filtered_df = df[df['sensor_id'] == sensor_id]
    result_json = filtered_df.to_json(orient='records')
    
    return result_json