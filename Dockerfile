FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN pip install -U pip \
    && pip install -Ur requirements.txt \
    && /code/manage.py collectstatic --noinput

COPY . /code/

CMD ["/code/bin/run.sh"]
