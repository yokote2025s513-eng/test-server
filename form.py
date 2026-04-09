from flask import Flask, request
import os
import requests

app = Flask(__name__)

GAS_URL = "https://script.google.com/macros/s/AKfycbyuuqxRzhMeapSgxp07Hyn7Xnka9H_YmkP36wTpP-U-PAiEEP-sm7u9qy62wT17fg/exec"

@app.route("/")
def home():
    return """
    <h1>アンケート</h1>
    <form action="/submit" method="post">
         名前:<br>
         <input type="text" name="name"><br><br>
         <input type="submit" value="送信">
    </form>
    """

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]

    requests.post(GAS_URL, json={"name": name})

    return f"送信ありがとう {name}!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10001))
    app.run(host="0.0.0.0", port=port)
