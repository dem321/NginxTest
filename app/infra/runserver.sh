poetry run python3 /app/manage.py makemigrations
poetry run python3 /app/manage.py migrate
poetry run python3 /app/manage.py collectstatic --noinput
poetry run python3 /app/manage.py createsuperuser --noinput
poetry run gunicorn --workers=9 --worker-class gthread --threads 16 --log-level DEBUG --timeout 360 -b 0.0.0.0:8000 NginxTest.wsgi
