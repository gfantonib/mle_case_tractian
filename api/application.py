#!/usr/bin/env python3

from flask import Flask, request, jsonify
import numpy as np
import csv
import os

app = Flask(__name__)

# File path for storing the data
csv_file_path = "sensor_data.csv"

# Initialize CSV file with headers if it doesn't exist
if not os.path.exists(csv_file_path):
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["sensor_id", "mean", "std_dev"])

@app.route("/<sensor_id>/fit", methods=["POST"])
def sensor_fit(sensor_id):
    data = request.get_json()
    
    # Get the list of values from the request
    values = data["values"]
    
    # Calculate mean and standard deviation
    mean = np.mean(values)
    std_dev = np.std(values)
    
    # Append the results to the CSV file
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([sensor_id, mean, std_dev])
    
    # Return the result
    result = {
        "sensor_id": sensor_id,
        "mean": mean,
        "std_dev": std_dev
    }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
