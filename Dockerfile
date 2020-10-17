FROM ubuntu:18.04

WORKDIR /app
RUN apt-get update && apt-get install -y python-pip 

ADD . /app

RUN pip install -r /requirements.txt
CMD ["/bin/bash"]