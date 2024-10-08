from flask import Flask, jsonify
import pandas as pd
import os
from config import PARQUET_FILE_PATH

from routes.index import index_blueprint
from routes.fit import fit_blueprint
from routes.weights import weights_blueprint
from routes.predict import predict_blueprint
from routes.adjust import adjust_blueprint

port = int(os.getenv("PORT", 5000))

app = Flask(__name__)
app.register_blueprint(index_blueprint)
app.register_blueprint(fit_blueprint)
app.register_blueprint(weights_blueprint)
app.register_blueprint(predict_blueprint)
app.register_blueprint(adjust_blueprint)

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

def create_parquet_database():
    try:
        if not os.path.exists(PARQUET_FILE_PATH):
            df = pd.DataFrame(columns=["sensor_id", "mean", "std_dev"])
            df.to_parquet(PARQUET_FILE_PATH, index=False)
    except Exception as e:
        print(f"Error creating Parquet file: {e}")
        exit(1)

if __name__ == "__main__":
    create_parquet_database()
    app.run(host="0.0.0.0", port=port, debug=True)
