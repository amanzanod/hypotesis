FROM python:3.8.3

LABEL maintainer="Antonio Manzano Díaz<amanzanod@uoc.edu>"

RUN apt-get update -y
RUN apt-get install python3-dev -y
RUN apt-get install default-libmysqlclient-dev -y

COPY requirements.txt .

RUN pip install -r requirements.txt

#CMD python manage.py migrate --noinput