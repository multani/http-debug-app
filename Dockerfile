FROM python:3.7-slim

ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir --upgrade poetry==1.0.2
WORKDIR /src
ADD poetry.lock pyproject.toml /src/
RUN poetry install

ADD . /src
ENTRYPOINT ["poetry", "run", "/src/app.py"]
