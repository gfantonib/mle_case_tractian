#!/usr/bin/env python3

import time
import pandas as pd
from math import sqrt

# ------------------------------ DRAFT ------------------------------
def draft(df: pd.DataFrame) -> float:
    draft_start_time = time.time()

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

    draft_end_time = time.time()
    draft_elapsed_time = draft_end_time - draft_start_time
    return draft_elapsed_time
# ------------------------------ DRAFT ------------------------------


# -------------------------- OPTMIZED DRAFT -------------------------
def optmized_draft(df: pd.DataFrame) -> float:
    # TRAIN

    # get start time
    optmized_draft_start_time = time.time()

    # remove unwanted columns
    df_light = df.drop(["_id", "createdAt", "params.duration", "params.sampRate", "params.timeStart", "temp"], axis=1)

    # create an object grouped by sensorId column
    sensor_groups = df_light.groupby("sensorId")

    # get the mean of each column of each group
    sensor_groups_means = sensor_groups.mean()

    # get the std dev of each column of each group
    sensor_groups_stds = sensor_groups.std()

    # PREDICT

    # set discriminator value
    new_value = 9e-2

    # create new boolean df that fit the condition
    result_df = new_value >= sensor_groups_means + 2*sensor_groups_stds

    # calculate and print elapsed time 
    optmized_draft_end_time = time.time()
    optmized_draft_elapsed_time = optmized_draft_end_time - optmized_draft_start_time
    return optmized_draft_elapsed_time
# -------------------------- OPTMIZED DRAFT -------------------------
