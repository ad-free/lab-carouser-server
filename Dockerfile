FROM python:3.8.2-alpine
MAINTAINER noname.spyware@gmail.com
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1
ENV WORK_PATH /code/

RUN apk add --update --no-cache mariadb-connector-c-dev \
	&& apk add --no-cache --virtual .build-deps \
		mariadb-dev \
		postgresql-dev \
		gcc \
		musl-dev

RUN mkdir $WORK_PATH
WORKDIR $WORK_PATH
COPY . $WORK_PATH
RUN mkdir $WORK_PATH/static
RUN mkdir $WORK_PATH/statics
RUN mkdir /media/logs
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations 
RUN python manage.py migrate


EXPOSE 8000
