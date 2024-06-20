FROM python:3.9-alpine

# dependencies
RUN apk update && \
    apk add --no-cache \
        build-base \
        libffi-dev \
        openssl-dev \
        bash \
        git \
        python3-dev \
        py-pip \
        gcc \
        libc-dev \
        make

RUN pip install unittest

WORKDIR /myproject

COPY . .

ENTRYPOINT ["tail", "-f", "/dev/null"]

# docker build -t tmotrs .