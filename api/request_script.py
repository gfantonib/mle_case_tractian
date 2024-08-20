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

# Define iter max
iter_max = 20

# Function to generate random float values
def generate_random_values(size):
    return np.round(np.random.uniform(low=0.0, high=100.0, size=size), 2).tolist()

# Function to send POST request with random data
def send_post_request(sensor_id):
    values = generate_random_values(4)  # Adjust the size as needed
    data = {"values": values}
    response = requests.post(fit_url.format(sensor_id=sensor_id), json=data)
    return response

    # While loop to continuously send requests
def request_loop():
    i = 0
    while i < iter_max:
        # Randomly pick a sensor ID
        sensor_id = random.choice(sensor_ids)
        
        # Send the POST request
        response = send_post_request(sensor_id)
        
        # Print the response from the server
        print(f"Response for sensor ID {sensor_id}: {response.status_code} - {response.json()}")

        i += 1

response = requests.get(weights_url.format(sensor_id = sensor_ids[3]))
df = pd.DataFrame(response.json())
print(df)
