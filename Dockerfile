FROM python:3

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY . .

CMD [ "python", "./bot.py" ]
