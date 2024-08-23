#!/bin/bash

IMAGE_NAME="my-flask-app"
CONTAINER_NAME="my-flask-container"
PORT=5000

# Check if the Docker image exists
if [[ "$(sudo docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]; then
    echo "Docker image $IMAGE_NAME not found. Building the image..."
    sudo docker build -t $IMAGE_NAME .
else
    echo "Docker image $IMAGE_NAME already exists."
fi

# Check if the container is running
if [[ "$(sudo docker ps -q -f name=$CONTAINER_NAME)" == "" ]]; then
    # If the container exists but is not running
    if [[ "$(sudo docker ps -aq -f name=$CONTAINER_NAME)" != "" ]]; then
        echo "Starting existing container $CONTAINER_NAME..."
        sudo docker start $CONTAINER_NAME
    else
        echo "Running new container $CONTAINER_NAME..."
        sudo docker run -d --name $CONTAINER_NAME -p $PORT:5000 $IMAGE_NAME
    fi
else
    echo "Container $CONTAINER_NAME is already running."
fi


