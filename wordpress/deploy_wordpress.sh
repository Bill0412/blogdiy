#!/usr/bin/env bash

echo "Installing docker..."
echo 'y\n' | apt install docker.io
echo "Docker is installed."
echo ""

## docker compose wordpress+mysql
echo "Downloading docker-compose.yml"
wget --no-check-certificate "https://raw.githubusercontent.com/Bill0412/sitediy/master/wordpress/stack.yml"
echo "The configuration file is ready."
echo ""

echo "Trying to run docker on port 80..."
# docker run --name "wp-port-"${LISTEN_PORT} -p ${LISTEN_PORT}:80 -d wordpress || { echo "Unable to deploy at port "${LISTEN_PORT}; exit 1; }
docker stack deploy -c stack.yml wp-80
echo "Worepress container listening on port 80."

## TODO: setup https

echo "Setup success!!!"