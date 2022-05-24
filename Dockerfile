FROM python:3.8-slim-buster

RUN mkdir -p /code
COPY requirements.txt /tmp/requirements.txt
RUN cd /code && python -m venv env && source env/bin/activate \
    && pip install -r /tmp/requirements.txt --no-cache-dir
COPY fiscal /code/fiscal
WORKDIR /code
CMD ["/bin/bash", "-c", "source env/bin/activate && python -m uvicorn fiscal.app:app"]