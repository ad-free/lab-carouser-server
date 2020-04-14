FROM python:3.8.2-alpine
RUN apk add --update --no-cache mariadb-connector-c-dev \
	&& apk add --no-cache --virtual .build-deps \
		mariadb-dev \
		postgresql-dev \
		gcc \
		musl-dev
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/