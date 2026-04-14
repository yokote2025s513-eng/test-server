from flask import Flask, request
import os
import requests

app = Flask(__name__)

GAS_URL = "https://script.google.com/macros/s/AKfycbymwaISEIDas9f3BzTzeDxoDrC7kghMlrF-BUjRFgO_3tCzpEH5SJhQQgXU0ajNEMLm/exec"

@app.route("/")
def home():
    return """
    <h1>サイズ回答フォーム</h1>
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
         
          ウィンドブレーカ下:<br>
         <select name="size2">
         <option value="S">S</option>
         <option value="M">M</option>
         <option value="L">L</option>
         <option value="XL">XL</option>
         </select><br><br>

          YOKOTE Tシャツ:<br>
         <select name="size3">
         <option value="S">S</option>
         <option value="M">M</option>
         <option value="L">L</option>
         <option value="XL">XL</option>
         </select><br><br>

          ジャージ上:<br>
         <select name="size4">
         <option value="S">S</option>
         <option value="M">M</option>
         <option value="L">L</option>
         <option value="XL">XL</option>
         </select><br><br>

          ジャージ下:<br>
         <select name="size5">
         <option value="S">S</option>
         <option value="M">M</option>
         <option value="L">L</option>
         <option value="XL">XL</option>
         </select><br><br>

         ユニフォーム上:<br>
         <input type="radio" name="uni1" value="ランシャツ"> ランシャツ<br>
         <input type="radio" name="uni1" value="セパ"> セパ<br><br>

         <input type="submit" value="送信">

    </form>
    """

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "")
    size1 = request.form.get("size1", "")
    size2 = request.form.get("size2", "")
    size3 = request.form.get("size3", "")
    size4 = request.form.get("size4", "")
    size5 = request.form.get("size5", "")
    uni1 = request.form.get("uni1", "")

    res = requests.post(GAS_URL, json={
        "name": name,
        "size1": size1,
        "size2": size2,
        "size3": size3,
        "size4": size4,
        "size5": size5,
        "uni1": uni1
        })

    return f"<h2>{res.text}</h2>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10001))
    app.run(host="0.0.0.0", port=port)