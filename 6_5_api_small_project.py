from flask import Flask, request, jsonify
app = Flask(__name__)

app.route("/create_db")
class database:
    def __init__(self, host, user, password, db_name):
        self.host = request.json("host")
        self.user = request.json("user")
        self.password = request.json("password")
        self.db_name = request.json("db_name")


    def create_db(self):
        try:
            import mysql.connector as connection
            mydb = connection.connect(host = self.host, user = self.user, password = self.password)
            cursor = mydb.cursor() # cursor
            query1 = "CREATE DATABASE {};".format(self.db_name)
            cursor.execute(query1)
            print("Database ", self.db_name, " is created")
        except Exception as e:
            print(e)

app.route("/create_table")
class table(database):
    def table_creation(self):
        try:
            import mysql.connector as connection
            mydb = connection.connect(host=self.host, user=self.user, password=self.password)
            cursor = mydb.cursor()  # cursor
            cursor.execute("USE DATABASE {}".format(self.db_name))  # use database
            table_name = request.json("create_table")
            cursor.execute("DROP TABLE IF EXISTS {};".format("table_name"))
            col1 = request.json("col1")
            col1_type = request.json("col1_type")
            col2 = request.json("col2")
            col2_type = request.json("col2_type")
            col3 = request.json("col3")
            col3_type = request.json("col3_type")
            query2 = "CREATE TABLE {} ({} {},{} {},{} {});".format(table_name, col1, col1_type, col2, col2_type,
                                                                   col3, col3_type)
            cursor.execute(query2)
            print("Table created successfully")
        except Exception as e :
            print(e)


app.route("/insert_data")
class insert(database):
    def insert_data(self):
        try:
            import mysql.connector as connection
            mydb = connection.connect(host=self.host, user=self.user, password=self.password)
            cursor = mydb.cursor()  # cursor
            cursor.execute("USE DATABASE {}".format(self.db_name))  # use database
            insert_table_name = request.json("insert_table_name")
            col1 = request.json("col1")
            col1_type = request.json("col1_type")
            col2 = request.json("col2")
            col2_type = request.json("col2_type")
            col3 = request.json("col3")
            col3_type = request.json("col3_type")
            query3 = "CREATE TABLE {} ({} {},{} {},{} {});".format(insert_table_name, col1, col1_type, col2, col2_type, col3,
                                                                   col3_type)
            cursor.execute(query3)
            print("Inserted data into table successfully.")
        except Exception as e:
            print(e)


app.route("/update_data")
class update(database):
    def update_table(self):
        try:
            import mysql.connector as connection
            mydb = connection.connect(host=self.host, user=self.user, password=self.password)
            cursor = mydb.cursor()  # cursor
            cursor.execute("USE DATABASE {}".format(self.db_name))  # use database
            query4 = request.json("write query to update")  # user will write query
            # UPDATE table_name SET col1-new_value1, col2=new_value2 WHERE condition;
            cursor.execute(query4)
            print("updated table successfully.")
        except Exception as e:
            print(e)


app.route("/delete_data")
class delete(database):
    def delete_data(self):
        try:
            import mysql.connector as connection
            mydb = connection.connect(host=self.host, user=self.user, password=self.password)
            cursor = mydb.cursor()  # cursor
            cursor.execute("USE DATABASE {}".format(self.db_name))  # use database
