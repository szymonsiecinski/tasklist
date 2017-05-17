config: python manage.py migrate
config: python manage.py collectstatic
web: gunicorn  --env DJANGO_SETTINGS_MODULE=TaskList.settings -b :80 TaskList.wsgi
