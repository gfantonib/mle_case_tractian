import pandas as pd

def read_parquet(file_path):
    try:
        return pd.read_parquet(file_path)
    except Exception as e:
        raise RuntimeError(f"Error reading Parquet file: {str(e)}")

def write_parquet(df, file_path):
    try:
        df.to_parquet(file_path, index=False)
    except Exception as e:
        raise RuntimeError(f"Error writing Parquet file: {str(e)}")
