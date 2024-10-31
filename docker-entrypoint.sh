#!/bin/bash

if [ "$1" == "django" ]; then

  until pg_isready -h db -p 5432 -U ${DB_USER}; do
      echo "Waiting for PostgreSQL to fully initialize..."
      sleep 5
  done

  # set -e
  shift
  exec "$@"
  
  python manage.py migrate
  python manage.py collectstatic --noinput
  python manage.py runserver 0.0.0.0:8000

fi
