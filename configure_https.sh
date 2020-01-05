#!/usr/bin/env bash

#TODO: install https certificate for docker

while getopts m:d: option
do
case "${option}"
in
m) MAIL=${OPTARG};;
d) DOMAIN=${OPTARG};;
esac
done

echo "Installing Certbot ..."
# apt-get install python-certbot-nginx -y
echo "Certbot Installed"

