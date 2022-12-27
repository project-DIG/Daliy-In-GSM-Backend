# importing base image
FROM python:3.10.5

# updating docker host or host machine
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# changing current working directory to /usr/src/app
WORKDIR /usr/src/app

# copying requirement.txt file to present working directory
COPY requirements.txt ./

# installing dependency in container
RUN pip install -r requirements.txt

# copying all the files to present working directory
COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000