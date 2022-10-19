FROM python:3.8-slim-buster
COPY . /Revisionwebsitev3
WORKDIR /Revisionwebsitev3
RUN pip install -r requirements.txt
EXPOSE 5090 
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ]