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
adjust_url = "http://127.0.0.1:5000/{sensor_id}/adjust"

iter_max = 20

def generate_random_values(size):
    return np.round(np.random.uniform(low=0.0, high=15.0, size=size), 2).tolist()

def send_post_request(sensor_id):
    values = generate_random_values(4)
    data = {"values": values}
    response = requests.post(fit_url.format(sensor_id=sensor_id), json=data)
    return response

def fit_request_loop():
    i = 0
    while i < iter_max:
        sensor_id = random.choice(sensor_ids)
        response = send_post_request(sensor_id)
        print(f"Response for sensor ID {sensor_id}: {response.status_code} - {response.json()}")
        i += 1

def weights_request_loop():
    for sensor in sensor_ids:
        response = requests.get(weights_url.format(sensor_id = sensor))
        df = pd.DataFrame(response.json())
        print(f"{df}\n")

def predict_request_loop():
    for sensor in sensor_ids:
        values = generate_random_values(1)
        data = {"values": values[0]}
        response = requests.post(predict_url.format(sensor_id = sensor), json=data)
        df_sensor_alert = pd.DataFrame({
            'sensor_id': [sensor] * len(response.json()),
            'alert': list(response.json().values())
        })
        print(f"{df_sensor_alert}\n")

def adjust_request_loop():
    for sensor in sensor_ids:
        data = {}
        response = requests.post(adjust_url.format(sensor_id = sensor), json=data)
        print(f"{response.json()}\n")


print("\n")
print(f"MAKE {iter_max} FIT REQUESTS (POST):\n")
fit_request_loop()
print("\n")

print(f"MAKE {len(sensor_ids)} WEIGHTS REQUESTS (GET):\n")
weights_request_loop()
print("\n")

print(f"MAKE {len(sensor_ids)} PREDICT REQUESTS (POST):\n")
predict_request_loop()
print("\n")

print(f"MAKE {len(sensor_ids)} ADJUST REQUESTS (POST):\n")
adjust_request_loop()
print("\n")

print(f"MAKE ANOTHER {len(sensor_ids)} WEIGHTS REQUESTS (GET):\n")
weights_request_loop()
print("\n")