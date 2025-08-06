

import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Berre1005"


)


mycursor=connection.cursor
mycursor.execute("Show databases")

for i in mycursor:
    print(x)




import mysql.connector

def insertProduct:
connection= mysql.connector.connect(host="localhost", user="root" , password="Berre1005" , database="node-app")
cursor=connection.cursor()
sql="İNSERT İNTO Products(name,price,imageUrl,description) VALUES (%s,%s)"
values=("Iphone 11",20000,"1 jpg","iyi telefon")

cursor.execute(sql,values)

try:
  connection.commit()

except mysql.connector.Error as err:
   print("Hata:", err)

finnaly:
connection.close()
print("database bağlantısı kapandı.")

insertProduct() 





import mysql.connector
from datetime import datetime
from connection import connection


class Student:
   
   def __init__(self,studentNumber,name,surname,birtdate,gender):
      self.studentNumber=studentNumber
      self.name=name
      self.surname=surname
      self.birthdate=birtdate
      self.gender=gender

    def saveStudent(self):
      sql="İNSERT İNTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s)"

ogrenciler=[
   ("101","Ahmet","Yılmaz",datetime.datetime(2005,5,17),"E"),
   ("102","Ali","can",datetime.datetime(2005,10,14),"E"),
   ("103","Canan","tan",datetime.datetime(2005,11,2),"K"),
   ("104","Bahar","Tokgöz",datetime.datetime(2005,9,22),"K")


]
