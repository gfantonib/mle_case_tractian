import pandas as pd
from data_access.parquet_manager import read_parquet

parquet_file_path = "sensor_data.parquet"

def process_predict(sensor_id, data):
    discriminator = data.get("values")

    if not isinstance(discriminator, (int, float)):
        return {"error": "Invalid input: value must be a number", "status": 400}

    try:
        df = read_parquet(parquet_file_path)
        df_sensor = df[df['sensor_id'] == sensor_id]
        
        if df_sensor.empty:
            return {"error": f"Sensor ID {sensor_id} not found", "status": 404}

        bool_series = 20 >= df_sensor["mean"] + 2*df_sensor["std_dev"]
        result_df = pd.DataFrame({
            'id': df_sensor['id'],
            'result': bool_series
        })
        
        return result_df.to_dict(orient='records')
    except Exception as e:
        return {"error": f"Error processing prediction: {str(e)}", "status": 500}
