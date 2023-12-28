#!/bin/bash
echo Running migrations
poetry run python manage.py migrate --noinput

echo Collectin staticfiles
poetry run python manage.py collectstatic --no-input --clear

echo Running server with gunicorn
poetry run gunicorn config.wsgi:application --bind 0.0.0.0:80 --workers 4 --threads 4 --access-logfile '-' --error-logfile '-' --log-level info


#TODO  https://djangostars.com/blog/django-pytest-testing/ + pytest -n <number of processes> + precommit
