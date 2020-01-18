#!/usr/bin/env bash
LISTEN_PORT=$1

echo "Installing docker..."
echo 'y\n' | apt install docker.io
echo "Docker is installed."
echo ""

## docker compose wordpress+mysql
echo "Downloading docker-compose.yml"
wget "https://raw.githubusercontent.com/Bill0412/sitediy/wordpress/wordpress/stack.yml"
echo "The configuration file is ready."
echo ""

echo "Trying to run docker on port "${LISTEN_PORT}"..."
# docker run --name "wp-port-"${LISTEN_PORT} -p ${LISTEN_PORT}:80 -d wordpress || { echo "Unable to deploy at port "${LISTEN_PORT}; exit 1; }
docker stack deploy -c stack.yml wp-${LISTEN_PORT}
echo "Worepress container listening on port "${LISTEN_PORT}"."

## TODO: setup https

echo "Setup success!!!"