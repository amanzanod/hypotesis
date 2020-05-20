FROM python:3.8.3

LABEL maintainer="Antonio Manzano Díaz<amanzanod@uoc.edu>"

ENV URL_PORT $URL_PORT

COPY requirements.txt .

RUN pip install -r requirements.txt
#RUN python manage.py migrate

CMD python manage.py runserver $URL_PORT