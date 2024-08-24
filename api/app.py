#!/usr/bin/env python3

from flask import Flask, jsonify
import pandas as pd
import os

from routes.index import index_blueprint
from routes.fit import fit_blueprint
from routes.weights import weights_blueprint
from routes.predict import predict_blueprint
from routes.adjust import adjust_blueprint

app = Flask(__name__)
app.register_blueprint(index_blueprint)
app.register_blueprint(fit_blueprint)
app.register_blueprint(weights_blueprint)
app.register_blueprint(predict_blueprint)
app.register_blueprint(adjust_blueprint)

parquet_file_path = "sensor_data.parquet"

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    try:
        if not os.path.exists(parquet_file_path):
            df = pd.DataFrame(columns=["id", "sensor_id", "mean", "std_dev"])
            df.to_parquet(parquet_file_path, index=False)
    except Exception as e:
        print(f"Error creating Parquet file: {e}")
        exit(1)

    app.run(host="0.0.0.0", port=5000, debug=True)
