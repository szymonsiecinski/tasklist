config: set DATABASE_URL=postgres://zrpidqwtwntmzm:e999de354bd00d11f6f593407eadaee046840446f0957458960747faf379b633@ec2-54-247-166-129.eu-west-1.compute.amazonaws.com:5432/d21kd5lf2t5t3o
config: python manage.py migrate
config: set DISABLE_COLLECTSTATIC=1
web: gunicorn TaskList.wsgi --log-file -
