import pandas as pd
from math import sqrt

df = pd.read_csv("../data/collects.csv")

# Train
unique_sensors = []
for s in df["sensorId"].tolist():
    if s not in unique_sensors:
        unique_sensors.append(s)


sensors_means = dict()
sensors_std = dict()
for s in unique_sensors:
    aux_df = df[df["sensorId"] == s]
    cols_mean = dict()
    cols_std = dict()
    for col in ["params.velRMS.x", "params.velRMS.y", "params.velRMS.z", "params.accelRMS.x", "params.accelRMS.y", "params.accelRMS.z"]:
        col_values = aux_df[col].tolist()
        col_sum = 0
        counter = 0
        for v in col_values:
            if not pd.isna(v):
                col_sum += v
                counter += 1
        cols_mean[col] = col_sum/counter

        col_std = 0
        counter = -1
        for v in col_values:
            if not pd.isna(v):
                col_std += (v-cols_mean[col])**2
                counter += 1
        
        cols_std[col] = sqrt(col_std/counter)

    sensors_means[s] = cols_mean
    sensors_std[s] = cols_std


# Predict
new_value = 9e-2


in_alert = dict()
for s in unique_sensors:
    cols_in_alert = dict()
    for col in ["params.velRMS.x", "params.velRMS.y", "params.velRMS.z", "params.accelRMS.x", "params.accelRMS.y", "params.accelRMS.z"]:
        if new_value >= sensors_means[s][col] +  2*sensors_std[s][col]:
            cols_in_alert[col] = True
        elif new_value < sensors_means[s][col] + 2*sensors_std[s][col]:
            cols_in_alert[col] = False

    in_alert[s] = cols_in_alert
