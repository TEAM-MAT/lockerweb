#!/bin/sh

cd /home/ubuntu/
sudo apt-get update -y
sudo apt install python3 -y
python3 -m venv ssulocker
source ./venv/ssulocker/bin/activate
cd ./lockerweb
sudo apt-get install python3-pip -y
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential -y
pip3 install mysqlclient
cp ./db.py ./ssulocker/ssulocker/db.py
pip3 install -r requirements.txt
#기본 세팅 끝

cd ~/lockerweb/ssulocker
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