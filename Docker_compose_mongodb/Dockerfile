FROM python:3.6.8-slim

ADD . /counter_app

WORKDIR /counter_app

ADD . .

RUN pip install -r requirements.txt

RUN chmod 644 manage.py

EXPOSE 5000

CMD ["python", "manage.py", "runserver"]


