
FROM python:3.10.6-alpine3.16
LABEL maintainer="mkudlinski1"

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /tmp/requirements.txt
COPY ./nutrition.csv /nutrition.csv
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --no-cache libstdc++ &&\
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps\
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
       --disabled-password \
       --no-create-home \
       django-user

ENV PATH="/py/bin:$PATH"

USER django-user