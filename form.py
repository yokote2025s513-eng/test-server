from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")  # ← route に修正
def home():
    return """
    <h1>アンケート</h1>
    <form action="/submit" method="post">
         名前:<br>
         <input type="text" name="name"><br><br>
         <input type="submit" value="送信">
    </form>
    """

@app.route("/submit", methods=["POST"])  # ← インデント外に出す
def submit():
    name = request.form["name"]

    print(name)

    return f"送信ありがとう {name}!"

port = int(os.environ.get("PORT", 10001))
app.run(host="0.0.0.0", port=port)
