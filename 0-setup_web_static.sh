#!/usr/bin/env bash
# This script installs nginx and sets it up for test runs

# update package lsi
sudo apt update -y

# install nginx
sudo apt install nginx -y

# create folders if they do not exits
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# create fake html file to test nginx
echo "This is a test: nginx up and runninig" > /data/web_static/releases/test/index.html

# create symbolic link that links current to test
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of /data/ folder to ubuntu user and group
sudo chown -hR ubuntu:ubuntu /data/

# update nginx to serve content
update="location /hbnb_static {\
	alias /data/web_static/current/;\
	index index.html;\
}"
sudo sed -i "/listen 80 default_server;/a $update" /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart
