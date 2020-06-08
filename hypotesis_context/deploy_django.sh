#!/bin/bash
echo "*** EXECUTING DJANGO HYPOTESIS CONTEXT ... ***"
echo "Wait for DB ..."
sleep 0m 40s
echo "40s"
sleep 0m 40s
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