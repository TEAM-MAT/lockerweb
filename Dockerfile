FROM ubuntu:latest

WORKDIR /home/ubuntu/lockerweb
COPY ./Design ./Design
COPY ./dump ./dump
COPY ./nginx_gunicorn ./nginx_gunicorn
COPY ./ssulocker ./ssulocker
COPY ./test ./test
COPY ./install_test.sh ./install_test.sh
COPY ./requirements.txt ./requirements.txt
RUN chmod +x install.sh
EXPOSE 80 8080
CMD ["bash","./install_test.sh"]