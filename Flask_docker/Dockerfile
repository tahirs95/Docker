FROM python:3.6.8-slim

RUN mkdir /opt/hello_app

WORKDIR /opt/hello_app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

RUN chmod 644 hello.py

CMD ["python", "hello.py" ]