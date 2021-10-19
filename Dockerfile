FROM python:3.9-slim

WORKDIR /opt/microservice/

COPY app/ /opt/microservice
COPY requirements.txt /opt/microservice/requirements.txt

RUN pip install -r /opt/microservice/requirements.txt

CMD ["python3", "/opt/microservice/main.py"]