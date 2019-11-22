FROM python:3.8.0-alpine3.10

WORKDIR /code

ENV APPLICATION_PORT 5000

RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

EXPOSE $APPLICATION_PORT

ENV FLASK_APP app.py
ENV FLASK_ENV development
ENV FLASK_DEBUG 0

ENTRYPOINT ["python", "-m", "flask", "run"]
