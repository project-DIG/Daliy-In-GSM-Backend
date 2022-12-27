FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get -y install vim && apt-get clean
RUN mkdir /code
ADD . /code

WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .