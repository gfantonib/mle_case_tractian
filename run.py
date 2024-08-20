#!/usr/bin/env python3

import pandas as pd
from tractian import Tractian

df = pd.read_csv("data/collects.csv")
new_value = 9e-2

sensor_alert = Tractian(df)
sensor_alert.clean_data()
sensor_alert.train()
sensor_alert.predict(new_value)

print(sensor_alert.get_result_df())