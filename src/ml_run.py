#!/usr/bin/env python3

import pandas as pd
from ml_class import mlModel

def prepare_data(df:pd.DataFrame):
	df_prepared = df.drop(["_id", "createdAt", "params.duration", "params.sampRate", "params.timeStart", "temp"], axis=1)
	return df_prepared

df = pd.read_csv("../data/collects.csv")
new_value = 9e-2
df_prepared = prepare_data(df)

sensor_alert = mlModel()
sensor_alert.train(df_prepared)
sensor_alert.predict(new_value)

print(sensor_alert.get_df_result())