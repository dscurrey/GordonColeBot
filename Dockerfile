FROM python:3

COPY bot.py bot.py
COPY quotegenerator.py quotegenerator.py
COPY quotes.txt quotex.txt
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "./bot.py" ]
