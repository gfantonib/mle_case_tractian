from data_access.parquet_manager import read_parquet, write_parquet
from config import PARQUET_FILE_PATH

def process_adjust(sensor_id):
    """
    Adjusts the mean value for a given sensor ID by a 10% increase.

    Args:
        sensor_id (str): The ID of the sensor.

    Returns:
        dict: A dictionary with a success message if the update is successful.
              If the sensor ID is not found or an error occurs, returns an error message and status code.
    """
    try:
        df = read_parquet(PARQUET_FILE_PATH)
        
        if sensor_id not in df['sensor_id'].values:
            return {"error": f"Sensor ID {sensor_id} not found", "status": 404}
        
        df.loc[df['sensor_id'] == sensor_id, 'mean'] *= 1.10
        write_parquet(df, PARQUET_FILE_PATH)
        
        return {"message": "Database updated successfully"}
    except Exception as e:
        return {"error": f"Error adjusting sensor data: {str(e)}", "status": 500}

