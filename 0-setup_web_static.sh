#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

# Path to the Nginx configuration file
NGINX_CONF="/etc/nginx/nginx.conf"

# The location block for serving hbnb_static
HBNB_STATIC_LOCATION="location /hbnb_static/ {
    alias /data/web_static/current/;
    index index.html;
    try_files \$uri \$uri/ =404;
}"


if ! command -v nginx > /dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install nginx -y
fi


# Creating necessary directories
mkdir -p /data/web_static/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/releases/test/

# Simple HTML file for testing
echo "Hello, this is a test page." > /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Add the location block to the config
echo -e "\n$HBNB_STATIC_LOCATION" >> "$NGINX_CONF"

nginx -s reload
