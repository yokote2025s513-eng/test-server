from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "server running"

@app.route("/test")
def test():
    return "this is test page"

port = int(os.environ.get("PORT",10000))
app.run(host="0.0.0.0",port=port)