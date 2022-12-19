from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    