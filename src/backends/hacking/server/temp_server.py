from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    password = request.args.get("password")
    email = request.args.get("email")
    time = datetime.now()