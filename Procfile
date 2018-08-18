release: python manage.py migrate
         python manage.py createsuperuser
web: gunicorn myproject.wsgi --log-file -