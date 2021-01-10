import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "9924721299",
  database = "atmdata"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE ")

#mycursor.execute("CREATE DATABASE atmdata")
