#!/bin/bash
echo "*** EXECUTING DJANGO HYPOTESIS MANAGER... ***"
echo "Wait for DB ..."
sleep 0m 30s
echo "30s"
sleep 0m 30s
echo "1m00s"
echo "Running ..."
# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput
# Apply database migrations
echo "Apply database migrations..."
python manage.py migrate --noinput
##python manage.py migrate --database=hypotesis_context --noinput
# Start server
echo "Starting server..."
python manage.py runserver "$1"
echo "*** EXECUTING DJANGO END > ***"