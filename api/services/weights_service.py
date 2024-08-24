from data_access.parquet_manager import read_parquet

parquet_file_path = "sensor_data.parquet"

def get_weights(sensor_id):
    try:
        df = read_parquet(parquet_file_path)
        filtered_df = df[df['sensor_id'] == sensor_id]
        
        if filtered_df.empty:
            return {"error": f"Sensor ID {sensor_id} not found", "status": 404}

        return filtered_df.to_dict(orient='records')
    except Exception as e:
        return {"error": f"Error retrieving sensor data: {str(e)}", "status": 500}
