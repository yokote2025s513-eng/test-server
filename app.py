from flask import flask

app = Flask(__name__)

@app.route("/")
def home():
    return "server running"

app.run(host="0.0.0.0",port=10000)