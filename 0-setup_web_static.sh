#!/usr/bin/env bash
# create web static for a server

sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo -e "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" > ./data/web_static/releases/test/index.html

if [ -L ./data/web_static/current ]; then
	rm ./data/web_static/current
fi
ln -s ./data/web_static/releases/test/ ./data/web_static/current
sudo chown -R ubuntu:ubuntu ./data

red_from="location / {"
red_to="location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sed -i "s#$red_from#$red_to#" /etc/nginx/sites-available/default
service nginx restart
