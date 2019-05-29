FROM python:3.6.8-slim

ADD . /app

WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

RUN chmod 644 app.py

EXPOSE 80

# CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80", "--workers", "4", "--reload"]


