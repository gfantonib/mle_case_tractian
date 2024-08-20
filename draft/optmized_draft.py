#!/usr/bin/env python3

# Imports
import time
import pandas as pd

# get data
df = pd.read_csv("../data/collects.csv")

# TRAIN

# get start time
start_time = time.time()

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
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds\n")

# print resulting df
print(result_df)