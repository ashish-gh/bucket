FROM python:3.8-slim

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:$PORT --threads=2 --workers=1  app.app:app