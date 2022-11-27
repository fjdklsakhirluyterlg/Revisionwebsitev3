FROM python:3.10.5

ADD . /Revisionwebsitev3
WORKDIR /Revisionwebsitev3

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5090"]