#!/usr/bin/env bash

apt install docker.io && echo "Docker is installed"
echo ""

docker pull wordpress && echo "wordpress image is ready"
echo ""

docker run --name wp0 80:80 -d wordpress || { echo "Unable to deploy at port 80"; exit 1; }

echo "Docker running on port 80"