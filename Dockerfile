FROM python:3.7-alpine

RUN pip install --no-cache-dir --upgrade bottle==0.12.13
WORKDIR /src
ADD . /src
ENTRYPOINT ["/src/app.py"]
