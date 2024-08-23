#!/usr/bin/env python3

from flask import Flask, jsonify
from routes.index import index_blueprint
from routes.fit import fit_blueprint
from routes.weights import weights_blueprint
from routes.predict import predict_blueprint
from routes.adjust import adjust_blueprint
import csv
import os

app = Flask(__name__)
app.register_blueprint(index_blueprint)
app.register_blueprint(fit_blueprint)
app.register_blueprint(weights_blueprint)
app.register_blueprint(predict_blueprint)
app.register_blueprint(adjust_blueprint)

csv_file_path = "sensor_data.csv"

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    try:
        if not os.path.exists(csv_file_path):
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["sensor_id", "mean", "std_dev"])
    except IOError as e:
        print(f"Error creating CSV file: {e}")
        exit(1)
    
    app.run(host="0.0.0.0", port=5000, debug=True)
