from data_access.parquet_manager import read_parquet, write_parquet

parquet_file_path = "sensor_data.parquet"

def process_adjust(sensor_id):
    try:
        df = read_parquet(parquet_file_path)
        
        if sensor_id not in df['sensor_id'].values:
            return {"error": f"Sensor ID {sensor_id} not found", "status": 404}
        
        df.loc[df['sensor_id'] == sensor_id, 'mean'] *= 1.10
        write_parquet(df, parquet_file_path)
        
        return {"message": "Database updated successfully"}
    except Exception as e:
        return {"error": f"Error adjusting sensor data: {str(e)}", "status": 500}
