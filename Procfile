config: python manage.py migrate
config: set DISABLE_COLLECTSTATIC=1
web: gunicorn  --env DJANGO_SETTINGS_MODULE=TaskList.settings -b :80 TaskList.wsgi
