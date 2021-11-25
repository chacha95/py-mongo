FROM python:3.8.2
LABEL maintainer="chacha, ckwlsgur20@naver.com"
ENV LC_ALL C.UTF-8
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHON_VERSION=3.8.2
RUN apt-get update \
    && apt-get install -y ca-certificates python3-dev apt-utils wget git openssh-client netbase curl subversion unzip vim \
    && rm -rf /var/lib/apt/lists/*

# uvicorn-gunicorn-fastapi
RUN pip3 install --no-cache-dir gunicorn uvicorn fastapi PyYaml uvloop httptools pytest

COPY src /home/src
COPY test /home/test
COPY challenges /home/challenges

WORKDIR /home/src
EXPOSE 80

# ENTRYPOINT ["bash", "/home/src/run.sh"]
