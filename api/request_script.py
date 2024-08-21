#!/usr/bin/env python3

import requests
import numpy as np
import random
import pandas as pd
import json

# Define the list of sensor IDs
sensor_ids = [
    "IAJ9206", "LZY4270", "MUR8453", "MXK6435", "MYD8706", 
    "MYS2071", "MZU6388", "NAH4736", "NAI1549", "NEW4797"
]

# Define the URL of the API
fit_url = "http://127.0.0.1:5000/{sensor_id}/fit"
weights_url = "http://127.0.0.1:5000/{sensor_id}/weights"
predict_url = "http://127.0.0.1:5000/{sensor_id}/predict"

# Define iter max
iter_max = 20

# Function to generate random float values
def generate_random_values(size):
    return np.round(np.random.uniform(low=0.0, high=20.0, size=size), 2).tolist()

# Function to send POST request with random data
def send_post_request(sensor_id):
    values = generate_random_values(4)  # Adjust the size as needed
    data = {"values": values}
    response = requests.post(fit_url.format(sensor_id=sensor_id), json=data)
    return response

# While loop to continuously send fit requests
def fit_request_loop():
    i = 0
    while i < iter_max:
        sensor_id = random.choice(sensor_ids)
        response = send_post_request(sensor_id)
        print(f"Response for sensor ID {sensor_id}: {response.status_code} - {response.json()}")

        i += 1

print("\n")
print(f"MAKE {iter_max} FIT REQUESTS (POST):\n")
fit_request_loop()
print("\n")

print(f"MAKE {len(sensor_ids)} WEIGHTS REQUESTS (GET):\n")
for sensor in sensor_ids:
    response = requests.get(weights_url.format(sensor_id = sensor))
    df = pd.DataFrame(response.json())
    print(df)
print("\n")

print(f"MAKE {len(sensor_ids)} PREDICT REQUESTS (POST):\n")
for sensor in sensor_ids:
    values = generate_random_values(1)
    data = {"values": values[0]}
    response = requests.post(predict_url.format(sensor_id = sensor), json=data)
    sensor_alert_df = pd.DataFrame({
        'sensor_id': [sensor] * len(response.json()),
        'alert': list(response.json())
    })
    print(sensor_alert_df)
print("\n")