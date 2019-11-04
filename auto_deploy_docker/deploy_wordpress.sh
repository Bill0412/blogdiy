#!/usr/bin/env bash

echo "Installing docker..."
echo 'y\n' | apt install docker.io
echo "Docker is installed."
echo ""

echo "Downloading Wordpress Docker image..."
docker pull wordpress
echo "Wordpress Docker image is ready."
echo ""

echo "Trying to run docker on port 80..."
docker run --name wp0 -p 80:80 -d wordpress || { echo "Unable to deploy at port 80"; exit 1; }
echo "Woredpress container listening on port 80."

echo "Setup success!!!"