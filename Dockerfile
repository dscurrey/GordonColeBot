FROM python:3.8.5-slim-buster

WORKDIR /gordoncole

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./bot.py" ]
