FROM ubuntu:20.04

WORKDIR /scripts

COPY . /scripts
RUN apt-get update

RUN apt-get install -y git

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

RUN pip install -r requirements.txt

CMD ["/bin/bash"]

