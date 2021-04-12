FROM python:3.9.0

WORKDIR /home/

RUN echo "testing123"

RUN git clone https://github.com/do-not-do-that/OLuck.git

WORKDIR /home/OLuck/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=butter.settings.deploy && python manage.py migrate --settings=butter.settings.deploy && gunicorn butter.wsgi --env DJANGO_SETTINGS_MODULE=butter.settings.deploy --bind 0.0.0.0:8000"]
