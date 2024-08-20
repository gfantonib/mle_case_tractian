#!/usr/bin/env python3

from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import csv
import os

app = Flask(__name__)

csv_file_path = "sensor_data.csv"

if not os.path.exists(csv_file_path):
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["sensor_id", "mean", "std_dev"])

@app.route("/<sensor_id>/fit", methods=["POST"])
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

@app.route("/<sensor_id>/fit", methods=["GET"])
def sensor_weights(sensor_id):

    df = pd.read_csv(csv_file_path)
    filtered_df = df[df['sensor_id'] == sensor_id]
    result_json = filtered_df.to_json(orient='records')
    
    return result_json

if __name__ == "__main__":
    app.run(debug=True)
