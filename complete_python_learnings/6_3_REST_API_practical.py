# Build flask API to create, add, insert and delete data into sql:

from flask import Flask , jsonify , request
app = Flask(__name__)

# this worked successfully:
# confirming connection :
@app.route("/confirming", methods = ['POST'])
def confirmation():
    user = request.json['user']
    host = request.json['host']
    password = request.json['password']
    import mysql.connector as con
    mysql = con.connect(host = host, user = user, password = password)
    cur = mysql.cursor()
    sh = cur.execute("show databases")
    fet = cur.fetchall()
    return fet


# worked but, it is creating with default name("db_name"), not creating db with user given name.
#database creation :
@app.route("/creating_db", methods = ['POST'])
def creating_database():
    user = request.json['user']
    host = request.json['host']
    password = request.json['password']
    import mysql.connector as con
    mysql = con.connect(host = host, user = user, password = password)
    cur = mysql.cursor()
    database = request.json['db_name']
    sh = cur.execute("create database datab")
    fet = cur.fetchall()
    return fet



# worked but same problem as db creation : 
# creating tabes :
@app.route("/creating_db", methods = ['POST'])
def creating_database():
    user = request.json['user']
    host = request.json['host']
    password = request.json['password']
    import mysql.connector as con
    mysql = con.connect(host = host, user = user, password = password)
    cur = mysql.cursor()
    table_ = request.json['table_']
    sh = cur.execute("create table table_")
    fet = cur.fetchall()
    return fet





if __name__ == '__main__':
    app.run()