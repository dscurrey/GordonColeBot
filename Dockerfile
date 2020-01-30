FROM python:3

RUN adduser -D gordoncole

WORKDIR /home/gordoncole

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY . .

CMD [ "python", "./bot.py" ]
