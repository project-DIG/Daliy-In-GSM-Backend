#!/bin/bash

# Migrate Database
python3 manage.py migrate --noinput

# Collect Staticfiles
python3 manage.py collectstatic --noinput

# Run Gunicorn (WSGI Server)
gunicorn daliyInGsm.wsgi:application --bind 0.0.0.0:8000