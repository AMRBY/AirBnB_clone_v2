#!/usr/bin/env bash
# create web static for a server

if (! dpkg-query -W "nginx" >/dev/null 2>&1); then
	sudo apt-get -y install nginx
fi
if [ ! -d ./data ]; then
	mkdir ./data/
	mkdir ./data/web_static/
	mkdir ./data/web_static/releases/
	mkdir ./data/web_static/shared/
	mkdir ./data/web_static/releases/test/
elif [ ! -d ./data/web_static ]; then
	mkdir ./data/web_static/
	mkdir ./data/web_static/releases/
	mkdir ./data/web_static/shared/
	mkdir ./data/web_static/releases/test/
elif [ ! -d ./data/web_static/releases ]; then
	mkdir ./data/web_static/releases/
	mkdir ./data/web_static/releases/test/
elif [ ! -d ./data/web_static/shared ]; then
	mkdir ./data/web_static/shared/
elif [ ! -d ./data/web_static/releases/test ]; then
	mkdir ./data/web_static/releases/test/
fi

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
