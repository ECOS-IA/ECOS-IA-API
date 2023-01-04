from flask import Flask,jsonify, request
import requests
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
import json
from datetime import datetime
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = os.environ["MYSQL_USER"]
app.config['MYSQL_PASSWORD'] = os.environ["MYSQL_PASSWORD"]
app.config['MYSQL_DB'] = 'ecosia'
 
mysql = MySQL(app)


@app.route('/alert/all')
def get_all_alerts():

  if request.args.get('order'):
    order_by = f"ORDER BY a.id {request.args['order'] if str.upper(request.args['order'])=='DESC' else 'ASC'}" 
  else:
    order_by=""
  
  cursor = mysql.connection.cursor()
  sql = f"""
  SELECT a.id, DATE_FORMAT(a.time, '%Y-%m-%d %H:%i:%s') as time, a.id_raspberry, a.label, b.zone
  FROM alert a INNER JOIN raspberry b ON a.id_raspberry=b.id
  {order_by}
  """
  
  cursor.execute(sql)
  results = cursor.fetchall()
  #x = results[0][1]
  #print("Raspberry " + x)
  cols = [desc[0] for desc in cursor.description]
  final_result = [dict(zip(cols,result)) for result in results]
  return jsonify(final_result)


@app.route('/raspberry/all')
def get_all_raspberrys():
  cursor = mysql.connection.cursor()
  sql = "SELECT * FROM raspberry"
  cursor.execute(sql)
  results = cursor.fetchall()
  #x = results[0][1]
  #print("Raspberry " + x)
  cols = [desc[0] for desc in cursor.description]
  final_result = [dict(zip(cols,result)) for result in results]
  return jsonify(final_result)



@app.route('/alert', methods=["POST"])
def alert():
  data = json.loads(request.data)
  cursor = mysql.connection.cursor()
  print(data)
  sql = f"INSERT INTO alert (time, id_raspberry, label) VALUES (%s, %s, %s)"
  cursor.execute(sql, (datetime.strptime(data["timestamp"],'%d-%m-%Y %H:%M:%S'), data['id_raspberry'],data['label']) )
  mysql.connection.commit()
  cursor.close()
  return ""


  #return requests.get("http://localhost:3000/api/", str(x)).content.decode("ascii")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=4000, debug=False)