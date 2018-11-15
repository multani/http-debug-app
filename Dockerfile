FROM python:3.6-slim

RUN pip install --no-cache-dir --upgrade pipenv
WORKDIR /src
ADD Pipfile* /src/
RUN pipenv --python /usr/local/bin/python install --system
ADD . /src
ENTRYPOINT ["/src/app.py"]
