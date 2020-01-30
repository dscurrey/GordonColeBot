FROM python:3

WORKDIR /gordoncole

COPY bot.py bot.py
COPY quotegenerator.py quotegenerator.py
COPY quotes.txt quotes.txt
COPY requirements.txt requirements.txt
VOLUME /gordoncole

RUN pip install -r requirements.txt

CMD [ "python", "./bot.py" ]
