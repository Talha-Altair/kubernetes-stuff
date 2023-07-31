FROM python:3.11.4-alpine3.17

ADD requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

ADD . .

CMD [ "python3", "app.py" ]