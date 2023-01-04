from flask import Flask,render_template, request
import requests
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
import json
from datetime import datetime

load_dotenv()

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = os.environ["MYSQL_USER"]
app.config['MYSQL_PASSWORD'] = os.environ["MYSQL_PASSWORD"]
app.config['MYSQL_DB'] = 'ecosia'
 
mysql = MySQL(app)


@app.route('/alert/all')
def get_all_alerts():
  cursor = mysql.connection.cursor()
  sql = "select id, DATE_FORMAT(time, '%Y-%m-%d %H:%i:%s') as time, id_raspberry, label from alert"
  cursor.execute(sql)
  results = cursor.fetchall()
  #x = results[0][1]
  #print("Raspberry " + x)

  ### to parse date to str: date.strftime('%d-%m-%Y %H:%M:%S') ###
  print(json.dumps(results))
  return ""

@app.route('/raspberry/all')
def get_all_raspberrys():
  cursor = mysql.connection.cursor()
  sql = "SELECT * FROM raspberry"
  cursor.execute(sql)
  results = cursor.fetchall()
  #x = results[0][1]
  #print("Raspberry " + x)
  print(json.dumps(results))
  return ""


@app.route('/alert', methods=["POST"])
def alert():
  data = json.loads(request.data)
  cursor = mysql.connection.cursor()
  print(data)
  sql = f"INSERT INTO alert (time, id_raspberry, label) VALUES (%s, %s, %s)"
  cursor.execute(sql, (data["timestamp"], data['id_raspberry'],data['label']) )
  mysql.connection.commit()
  cursor.close()
  return ""


  #return requests.get("http://localhost:3000/api/", str(x)).content.decode("ascii")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=4000, debug=True)