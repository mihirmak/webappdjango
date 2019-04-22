FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN pip3 install --upgrade setuptools
RUN apt install default-libmysqlclient-dev
COPY . /my_app_dir
WORKDIR /my_app_dir
RUN pip3 install -r requirements.txt

