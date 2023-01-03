from flask import Flask,render_template, request
import requests
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = os.environ["MYSQL_USER"]
app.config['MYSQL_PASSWORD'] = os.environ["MYSQL_PASSWORD"]
app.config['MYSQL_DB'] = 'ecosia'
 
print(app.config)
mysql = MySQL(app)


@app.route('/')
def alert():
  cursor = mysql.connection.cursor()
  sql = "SELECT * FROM capteur"
  cursor.execute(sql)
  results = cursor.fetchall()
  x = results[0][1]
  print("Raspberry " + x)

  #return requests.get("http://localhost:3000/api/", str(x)).content.decode("ascii")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=4000, debug=True)