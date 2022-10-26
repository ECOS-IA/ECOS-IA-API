from flask import Flask
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db = pymysql.connect(host="localhost", user="root", password="", database="ecosia")

@app.route("/")
def hello():
  cursor = db.cursor()
  sql = "SELECT * FROM capteur"
  cursor.execute(sql)
  results = cursor.fetchall()
  print(results[0])
  return "az"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000, debug=True)