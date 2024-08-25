import pandas as pd
import numpy as np
from data_access.parquet_manager import read_parquet, write_parquet

parquet_file_path = "sensor_data.parquet"

def process_fit(sensor_id, data):
    """
    Processes the fit request for a given sensor ID.

    Args:
        sensor_id (str): The ID of the sensor.
        data (dict): A dictionary containing the values for mean and standard deviation calculations.

    Returns:
        dict: A dictionary containing the results with 'id', 'sensor_id', 'mean', and 'std_dev'.
              If there's an error, returns an error message and status code.
    """
    values = data.get("values")

    if not isinstance(values, list) or not all(isinstance(x, (int, float)) for x in values):
        return {"error": "Invalid input: values must be a list of numbers", "status": 400}
    if len(values) == 0:
        return {"error": "Empty list of values", "status": 400}

    try:
        mean = np.mean(values)
        std_dev = np.std(values)
    except Exception as e:
        return {"error": f"Error calculating statistics: {str(e)}", "status": 500}

    try:
        df = read_parquet(parquet_file_path)

        new_row = pd.DataFrame({'sensor_id': [sensor_id], 'mean': [mean], 'std_dev': [std_dev]})
        df = pd.concat([df, new_row], ignore_index=True)

        write_parquet(df, parquet_file_path)

        return {"sensor_id": sensor_id, "mean": mean, "std_dev": std_dev}
    except Exception as e:
        return {"error": f"Error updating Parquet file: {str(e)}", "status": 500}
