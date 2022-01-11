FROM python:3.9-alpine
RUN apk update
WORKDIR /app
COPY . .
RUN pip3 install pipenv
RUN pipenv install --deploy --ignore-pipfile
CMD pipenv run python main.py
