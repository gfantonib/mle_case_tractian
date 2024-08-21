from flask import Blueprint, request, jsonify
import numpy as np
import pandas as pd

fit_blueprint = Blueprint("fit", __name__)

csv_file_path = "sensor_data.csv"

@fit_blueprint.route("/<sensor_id>/fit", methods=["POST"])
def sensor_fit(sensor_id):

    data = request.get_json()
    values = data["values"]
    mean = np.mean(values)
    std_dev = np.std(values)

    df = pd.read_csv(csv_file_path)
    
    if sensor_id in df['sensor_id'].values:
        df.loc[df['sensor_id'] == sensor_id, ['mean', 'std_dev']] = [mean, std_dev]
    else:
        new_row = pd.DataFrame({'sensor_id': [sensor_id], 'mean': [mean], 'std_dev': [std_dev]})
        df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(csv_file_path, index=False)
    
    result = {
        "sensor_id": sensor_id,
        "mean": mean,
        "std_dev": std_dev
    }
    
    return jsonify(result)