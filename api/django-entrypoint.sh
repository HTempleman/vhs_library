#!/bin/sh
echo Running Django Migrations.
cd vhs_api
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py migrate --fake vhs_library                  
python manage.py collectstatic --noinput 


echo Starting Gunicorn
gunicorn vhs_api.wsgi:application --name vhs_api --bind 127.0.0.1:8000 --workers 1 --daemon
echo Starting Envoy Reverse Proxy
cd ..
envoy -c django-service-envoy.yaml --service-cluster vhs_django


