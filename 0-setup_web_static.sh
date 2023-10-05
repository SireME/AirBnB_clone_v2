#!/usr/bin/env bash
# This script installs nginx and sets it up for test runs

# update package lsi
sudo apt update

# install nginx
sudo apt install nginx -y

# create folders if they do not exits
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# create fake html file to test nginx
echo "This is a test: nginx up and runninig" > /data/web_static/releases/test/index.html

# create symbolic link that links current to test
target=/data/web_static/releases/test/
link_name=/data/web_static/current

if [ -e "$link_name" ]; then
	# delete symbolic link if it already exists
	sudo rm "$link_name"
fi
# create symbolic link
sudo ln -s "$target" "$link_name"

# give ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# update nginx to serve content
update="location /hbnb_static {\
	alias /data/web_static/current/;\
	index index.html;\
}"
sed -i "/listen 80;/a $update" /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart
