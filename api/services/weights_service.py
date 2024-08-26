from data_access.parquet_manager import read_parquet
from config import PARQUET_FILE_PATH

def get_weights(sensor_id):
    """
    Retrieves weights for a given sensor ID from the Parquet file.

    Args:
        sensor_id (str): The ID of the sensor.

    Returns:
        dict: A dictionary containing sensor data or an error message if the sensor ID is not found.
              Status codes included in case of errors.
    """
    try:
        df = read_parquet(PARQUET_FILE_PATH)
        filtered_df = df[df['sensor_id'] == sensor_id]
        
        if filtered_df.empty:
            return {"error": f"Sensor ID {sensor_id} not found", "status": 404}

        return filtered_df.to_dict(orient='index')
    except Exception as e:
        return {"error": f"Error retrieving sensor data: {str(e)}", "status": 500}
