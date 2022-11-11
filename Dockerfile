#!/bin/bash
FROM python:3.8-slim-buster

RUN mkdir -p /app
WORKDIR /app 
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python3-gdbm
# install dependencies
RUN pip install --upgrade pip && pip install uvicorn
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
# copy project
COPY . /app
RUN pip install -e .
RUN pip uninstall -y bson
RUN pip uninstall -y pymongo
RUN pip install pymongo==3.12.3
RUN pip uninstall -y  flask_openapi3
RUN pip install flask_mailing
RUN pip install passlib
RUN pip install requests
RUN pip install "git+https://github.com/rajat45mishra/flaskopenapi.git#egg=flask-openapi3"
EXPOSE 8000
CMD ["uvicorn","infrastructure.server.app.wsgi:app","--workers","4","--host","0.0.0.0","--port","8000"]
