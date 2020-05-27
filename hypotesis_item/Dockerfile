FROM hypotesis_django:latest

LABEL maintainer="Antonio Manzano Díaz<amanzanod@uoc.edu>"

ENV URL_PORT $URL_PORT
ENV HYP_ITEM_SUPER_USER $HYP_ITEM_SUPER_USER
ENV HYP_ITEM_SUPER_USER_EMAIL $HYP_ITEM_SUPER_USER_EMAIL
ENV HYP_ITEM_SUPER_USER_PASS $HYP_ITEM_SUPER_USER_PASS

COPY requirements.txt .
COPY deploy_django.sh .

RUN pip install -r requirements.txt

CMD /bin/bash deploy_django.sh $URL_PORT $HYP_ITEM_SUPER_USER $HYP_ITEM_SUPER_USER_EMAIL $HYP_ITEM_SUPER_USER_PASS