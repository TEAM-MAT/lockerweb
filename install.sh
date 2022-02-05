#!/bin/sh

#nginx 이전에 설치해줘야할듯...아시아 -> 도쿄 시간대 -> 서울 
cd /home/ubuntu/
sudo apt-get update -y
sudo apt install python3 -y
sudo apt install python3.8-venv -y
sudo apt-get install python3-pip -y
pip3 install gunicorn
mkdir venv
cd ./venv
python3 -m venv ssulocker
chmod +x ./ssulocker/bin/activate
./ssulocker/bin/activate
cd /home/ubuntu/lockerweb
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential -y
pip3 install mysqlclient
#cp ./db.py ./ssulocker/ssulocker/db.py
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