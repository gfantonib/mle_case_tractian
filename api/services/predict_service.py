from data_access.parquet_manager import read_parquet

parquet_file_path = "sensor_data.parquet"

def process_predict(sensor_id, data):
    """
    Processes a prediction request for a given sensor ID.

    Args:
        sensor_id (str): The ID of the sensor.
        data (dict): A dictionary containing the discriminator value for the prediction.

    Returns:
        dict: A dictionary containing the prediction results.
              If there's an error, returns an error message and status code.
    """
    discriminator = data.get("values")

    if not isinstance(discriminator, (int, float)):
        return {"error": "Invalid input: value must be a number", "status": 400}

    try:
        df = read_parquet(parquet_file_path)
        df_sensor = df[df['sensor_id'] == sensor_id]
        
        if df_sensor.empty:
            return {"error": f"Sensor ID {sensor_id} not found", "status": 404}

        bool_series = discriminator >= df_sensor["mean"] + 2*df_sensor["std_dev"]
        return bool_series.to_dict()
    
    except Exception as e:
        return {"error": f"Error processing prediction: {str(e)}", "status": 500}
