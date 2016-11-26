FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && sudo apt-get -y install netcat \
    && mkdir /code

WORKDIR /code
COPY requirements.txt /code/

RUN pip install -U pip && pip install -Ur requirements.txt
COPY . /code/

EXPOSE 8000
COPY entrypoint.sh /
VOLUME /code/public

CMD ["/entrypoint.sh"]
