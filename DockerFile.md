# It is a file with instruction and argument.
# It can have any base package
FROM ubuntu 

RUN apt-get update
RUN apt-get install -y python python-pip
RUN pip install flask

COPY app.py /opt/app.python

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0
