FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdire /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
