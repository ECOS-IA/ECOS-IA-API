from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ecosia'
 
mysql = MySQL(app)

@app.route('/')
def hello():
  return render_template('Index.html')

@app.route('/alert')
def alert():
  cursor = mysql.connection.cursor()
  sql = "SELECT * FROM capteur"
  cursor.execute(sql)
  results = cursor.fetchall()
  x = results[0][1]
  print("Capteur" + x)
  return "Capteur : " + str(x)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000, debug=True)