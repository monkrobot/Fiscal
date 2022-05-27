FROM python:3.8-slim-buster

RUN mkdir -p /code
COPY requirements.txt /tmp/requirements.txt
RUN cd /code
COPY fiscal /code/fiscal
WORKDIR /code

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r /tmp/requirements.txt --no-cache-dir
CMD python3 -m uvicorn --host 0.0.0.0 fiscal.app:app
