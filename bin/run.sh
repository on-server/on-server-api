#!/usr/bin/env bash

set -e

./manage.py migrate

uwsgi --ini uwsgi.ini
