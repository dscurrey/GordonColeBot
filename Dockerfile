FROM python:3.8.5-slim-buster

WORKDIR /gordoncole

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY bot.py bot.py
COPY quotegenerator.py quotegenerator.py
COPY quotes.txt quotes.txt
VOLUME /gordoncole

CMD [ "python", "./bot.py" ]
