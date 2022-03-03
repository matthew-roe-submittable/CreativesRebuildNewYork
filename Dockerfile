FROM python:3.9-alpine
RUN apk update
WORKDIR /app
COPY . .
# RUN pip3 install
RUN python3 -m venv /venv
CMD source venv/bin/activate
# RUN pipenv install --deploy --ignore-pipfile
RUN pip install -r requirements.txt
CMD run python main.py

# docker run creatives:latest