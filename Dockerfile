FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN pip install -U pip && pip install -Ur requirements.txt
COPY . /code/

RUN python manage.py collectstatic --noinput

COPY entrypoint.sh /
CMD ["/entrypoint.sh"]
