#!/usr/bin/env bash
LISTEN_PORT=$1

echo "Installing docker..."
echo 'y\n' | apt install docker.io
echo "Docker is installed."
echo ""

## TODO: modify this to wordpress+mysql
echo "Downloading docker-compose.yml"
wget "https://raw.githubusercontent.com/Bill0412/sitediy/wordpress/wordpress/docker-compose.yml"
echo "The configuration file is ready."
echo ""

echo "Trying to run docker on port "${LISTEN_PORT}"..."
# docker run --name "wp-port-"${LISTEN_PORT} -p ${LISTEN_PORT}:80 -d wordpress || { echo "Unable to deploy at port "${LISTEN_PORT}; exit 1; }
docker swarm init
docker stack deploy -c docker-compose.yml wp-${LISTEN_PORT}
echo "Woredpress container listening on port "${LISTEN_PORT}"."

## TODO: setup https

echo "Setup success!!!"