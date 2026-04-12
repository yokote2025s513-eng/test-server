from flask import Flask, request
import os
import requests

app = Flask(__name__)

GAS_URL = "https://script.google.com/macros/s/AKfycbyL0O1jPIiSb_kLNUAkgywSYazZJKUhhe8E5cAzrCoS9_4t_ZRbltef5Y3LBc8Mo79O/exec"

@app.route("/")
def home():
    return """
    <h1>サイズ解答フォーム</h1>
    <form action="/submit" method="post">
         名前:<br>
         <input type="text" name="name"><br><br>
         ウィンドブレーカ上:<br>
         <select name="size1">
         <option value="S">S</option>
         <option value="M">M</option>
         <option value="L">L</option>
         <option value="XL">XL</option>
         </select><br><br>
         
         背番号:<br>
         <input type="number" name="number">
         <input type="submit" value="送信">
    </form>
    """

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "")
    student_id = request.form.get("student_id", "")
    word = request.form.get("word", "")
    number = request.form.get("number", "")


    res = requests.post(GAS_URL, json={
        "name": name,
        "id": student_id,
        "word": word,
        "number": number
    })

    return f"<h2>{res.text}</h2>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10001))
    app.run(host="0.0.0.0", port=port)