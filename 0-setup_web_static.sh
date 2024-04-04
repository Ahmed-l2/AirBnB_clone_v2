#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

# Checks if nginx is installed or not
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
echo "HELLO WORLD!" > /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Add the location block to the config
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart NGINX server
sudo service nginx restart
