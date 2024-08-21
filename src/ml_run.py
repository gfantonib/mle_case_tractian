#!/usr/bin/env python3

import pandas as pd
from ml_class import mlModel

df = pd.read_csv("../data/collects.csv")
new_value = 9e-2

sensor_alert = mlModel(df)
sensor_alert.prepare_data()
sensor_alert.train()
sensor_alert.predict(new_value)

print(sensor_alert.get_result_df())