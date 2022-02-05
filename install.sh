#!/bin/sh

cd /home/ubuntu/
python3 -m venv ssulocker
source ./venv/ssulocker/bin/activate
sudo apt-get update
sudo apt install python3
cd ./lockerweb
sudo apt-get install python3-pip
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip3 install mysqlclient
cp ./db.py ./ssulocker/ssulocker/db.py
pip3 install -r requirements.txt
#기본 세팅 끝

cd ./ssulocker
python3 manage.py migrate

#gunicorn file
cp /home/ubuntu/lockerweb/nginx_gunicorn/ssulocker.env /home/ubuntu/venv/ssulocker.env
cp /home/ubuntu/lockerweb/nginx_gunicorn/ssulocker.service /etc/systemd/system/ssulocker.service
sudo systemctl start ssulocker.service
sudo systemctl status ssulocker.service
sudo systemctl enable ssulocker.service

#nginx
cp /home/ubuntu/lockerweb/nginx_gunicorn/ssulocker /etc/nginx/sites-available/ssulocker
sudo rm /etc/nginx/sites-enabled/default
cd /etc/nginx/sites-enabled
sudo ln -s /etc/nginx/sites-available/ssulocker
sudo systemctl restart nginx