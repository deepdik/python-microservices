# Dockerfile
FROM python:3.7

## creating app dir in  docker image base location
WORKDIR /app

## copy  command location's(docker run) all files to /app inside docker image
COPY . .
## go to /app/service_1 folder inside docker image
WORKDIR /app/service_2

## inastall in docker
RUN pip install -r requirements.txt

CMD python3 run.py