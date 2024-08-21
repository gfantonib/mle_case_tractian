#!/usr/bin/env python3

from flask import Flask
from routes.index import index_blueprint
from routes.fit import fit_blueprint
from routes.weights import weights_blueprint
from routes.predict import predict_blueprint
import csv
import os

app = Flask(__name__)
app.register_blueprint(index_blueprint)
app.register_blueprint(fit_blueprint)
app.register_blueprint(weights_blueprint)
app.register_blueprint(predict_blueprint)

csv_file_path = "sensor_data.csv"


if __name__ == "__main__":
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["sensor_id", "mean", "std_dev"])
    app.run(debug=True)
