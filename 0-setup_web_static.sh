#!/usr/bin/env bash
# create web static for a server

apt-get -y install nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "Holberton School" > /data/web_static/releases/test/index.html
if [ -L /data/web_static/current ]; then
	rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
red_from="location / {"
red_to="location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n"
sed -i "s#$red_from#$red_to#" /etc/nginx/sites-available/default
service nginx restart
