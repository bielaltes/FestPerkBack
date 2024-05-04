FROM python:3.12

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN apt update
RUN apt-get install cron -y && touch /var/log/cron.log

RUN pip install psycopg2-binary


RUN pip install django-cors-headers

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Set up Django and PostgreSQL environment variables
ENV DJANGO_SETTINGS_MODULE=FestPerk.settings
ENV DATABASE_URL=postgres://username:password@db_host:5432/db_name

EXPOSE 8000

CMD ["python", "/app/FestPerk/manage.py", "migrate"]

ENTRYPOINT ["python", "/app/FestPerk/manage.py", "runserver", "0.0.0.0:8000"]
