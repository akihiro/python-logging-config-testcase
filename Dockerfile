FROM python:3.9
COPY ./ /tests/
WORKDIR /tests/
RUN python3 test.py
