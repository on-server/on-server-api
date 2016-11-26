FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN pip install -U pip && pip install -Ur requirements.txt
COPY . /code/

EXPOSE 8000
COPY entrypoint.sh /
VOLUME /code/public

CMD ["/entrypoint.sh"]
