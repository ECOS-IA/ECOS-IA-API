from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ecosia'
 
mysql = MySQL(app)

@app.route('/alerts')
def alert():
  cursor = mysql.connection.cursor()
  sql = "SELECT alert.id, time, zone FROM alert join capteur on alert.id_capteur = capteur.id"
  cursor.execute(sql)
  results = cursor.fetchall()

  tup = (results[0][0], str(results[0][1]), results[0][2])
  jsonObj = json.dumps(tup)

  return jsonObj

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000, debug=True)