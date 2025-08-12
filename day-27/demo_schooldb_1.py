

import mysql.connector
from datetime import datetime 


print("DB connection'ı kuruluyor ...")
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Berre1005",
    database="schooldb")

mycursor=connection.cursor()

print("Connection Kuruldu..!!")

sql="INSERT INTO student(StudentNumber,name,surname,birthdate,gender) VALUES(%s,%s,%s,%s,%s)"

ogrenciler=[
   ("301","Ahmet","Yilmaz",datetime(2005,5,17),"E"),
   ("302","Ali","can",datetime(2005,10,14),"E"),
   ("303","Canan","tan",datetime(2005,11,2),"K"),
   ("304","Bahar","Tokgöz",datetime(2005,9,22),"K")


]


try:
   mycursor.executemany(sql, ogrenciler)

   connection.commit()
   print(f'{mycursor.rowcount} tane kayit eklendi.')

except mysql.connector.Error as err:
   print("Hata:", err)
finally:
   connection.close() 


