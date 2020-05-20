FROM python:3.8.3

LABEL maintainer="Antonio Manzano Díaz <amanzanod@uoc.edu>"

#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt

# Puerto HTTP por defecto para uWSGI
#ARG HYPOTESIS_MANAGER_HTTP_PORT=8000
#ENV HYPOTESIS_MANAGER_HTTP_PORT=$HYPOTESIS_MANAGER_HTTP_PORT

WORKDIR /usr/src/app

#ENV PROJECT_ROOT=/srv
#WORKDIR $PROJECT_ROOT

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR

CMD ["python", "manage.py", "runserver 0.0.0.0:8000"]