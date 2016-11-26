#!/usr/bin/env bash

set -e

while ! nc -w 1 -z ${DB_HOST} ${DB_PORT}; do sleep 1; done

python manage.py migrate
python manage.py collectstatic --noinput

uwsgi --ini uwsgi.ini
