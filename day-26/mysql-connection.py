import mysql.connector


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Berre1005"

)
print(mydb)

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")



#mydatabase=mydb




import mysql.connector

connection=mysql.connector.connect(

host="localhost",
user="root",
password="Berre1005",
database="schooldb"

)

mycursor=connection.cursor()

mycursor.execute("Show databases")

for i in mycursor:
    print(i)

