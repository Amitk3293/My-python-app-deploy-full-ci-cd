# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install flask

COPY MainScores.py .
COPY requirements.txt .
COPY Scores.txt .

EXPOSE 5000

VOLUME [ "/app" ]

ENTRYPOINT [ "python3", "MainScores.py" ]

RUN echo "This Flask i exposed on port 5000"

# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

VOLUME [ "/app" ]

EXPOSE 8000

RUN echo 0 > Scores.txt MainScores.py

ENTRYPOINT [ "python3", "MainGame.py" ]

RUN echo "WOG app is exposed on port 8000"
