from flask import Flask, request
import os
import requests

app = Flask(__name__)

GAS_URL = "https://script.google.com/macros/s/AKfycbyGeA6ZeSzcxmxMTUJRWyF4OIDCKy7p7j_BJ7XdgQDZj8zYe-4IV-xWr3RamOxF8RNp/exec"

@app.route("/")
def home():
    return """
    <h1>アンケート</h1>
    <form action="/submit" method="post">
         名前:<br>
         <input type="text" name="name"><br><br>
         出席番号:<br>
         <input type="number" name="id"><br><br>
         背ネーム:<br>
         <input type="text" name="word"><br><br>
         背番号:<br>
         <input type="number" name="number">
         <input type="submit" value="送信">
    </form>
    """

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    id = request.form["id"]
    word = request.form["word"]
    number = request.form["number"]

    requests.post(GAS_URL, json={"name": name,"id": id,"word": word,"number": number})

    return f"送信ありがとう!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10001))
    app.run(host="0.0.0.0", port=port)