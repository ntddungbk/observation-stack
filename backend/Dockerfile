FROM python:3.11-slim

RUN python -m pip install pip --upgrade
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app