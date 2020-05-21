#!/bin/bash
echo "*** EXECUTING DJANGO ... ***"
echo "Wait for DB ..."
sleep 0m 15s
echo "15s"
sleep 0m 15s
echo "30s"
sleep 0m 15s
echo "45s"
sleep 0m 15s
echo "Running ..."
# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput
# Apply database migrations
echo "Apply database migrations..."
python manage.py migrate --noinput
# Start server
echo "Starting server..."
python manage.py runserver "$1"
echo "*** EXECUTING DJANGO END > ***"