#!/bin/sh

cd /root/
apt-get update -y
apt install python3 -y
apt install python3.8-venv -y
python3 -m venv ssulocker
source ./venv/ssulocker/bin/activate
cd ./lockerweb
apt-get install python3-pip -y
apt-get install python3-dev default-libmysqlclient-dev build-essential -y
pip3 install mysqlclient
#cp ./db.py ./ssulocker/ssulocker/db.py
pip3 install -r requirements.txt
#기본 세팅 끝

cd ./ssulocker
python3 manage.py migrate

#gunicorn file
cp /root/lockerweb/nginx_gunicorn/ssulocker.env /home/ubuntu/venv/ssulocker.env
cp /root/lockerweb/nginx_gunicorn/ssulocker.service /etc/systemd/system/ssulocker.service
systemctl start ssulocker.service
systemctl status ssulocker.service
systemctl enable ssulocker.service

#nginx
cp /root/lockerweb/nginx_gunicorn/ssulocker /etc/nginx/sites-available/ssulocker
rm /etc/nginx/sites-enabled/default
cd /etc/nginx/sites-enabled
ln -s /etc/nginx/sites-available/ssulocker
systemctl restart nginx