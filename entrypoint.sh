#!/bin/sh

# Wait for MySQL to be ready (optional but smart for Compose)
echo "Waiting for MySQL to be ready..."
while ! netcat -z db 3306; do
  sleep 1
done

echo "MySQL is up. Running migrations..."
# Run database migrations
python manage.py makemigrations
python manage.py makemigrations backend
python manage.py migrate
python manage.py migrate backend

# Run Django development server
python manage.py runserver 0.0.0.0:8000