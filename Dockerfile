FROM ubuntu:latest

WORKDIR /home/ubuntu
COPY . ./lockerweb

CMD ["./install.sh"]