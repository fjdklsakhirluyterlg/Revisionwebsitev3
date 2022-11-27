FROM python:3.10.5

WORKDIR /app

COPY ./requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5090"]