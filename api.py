from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
import json

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ecosia'
 
mysql = MySQL(app)

@app.route('/allAlerts')
def allAlerts():
  cursor = mysql.connection.cursor()
  sql = "SELECT alert.id, time, zone FROM alert join capteur on alert.id_capteur = capteur.id order by alert.id; "
  cursor.execute(sql)
  results = cursor.fetchall()
  x = [{"id": x, "time": y, "zone": z} for x, y, z in results]
  return x

@app.route('/')
def alert():
  cursor = mysql.connection.cursor()
  sql = "SELECT alert.id, time, zone FROM alert join capteur on alert.id_capteur = capteur.id order by alert.id desc limit 1"
  cursor.execute(sql)
  results = cursor.fetchall()
  x = [{"id": x, "time": y, "zone": z} for x, y, z in results]
  return x

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=4000, debug=True)