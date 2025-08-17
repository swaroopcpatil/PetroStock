import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="S#@98wrft45"
)

c = mydb.cursor()
c.execute("CREATE DATABASE PetrolPump_Management")