
    




import mysql.connector
from datetime import datetime 

print("DB connection'ı kuruluyor ...")

# Veritabanına bağlan
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Berre1005",
    database="schooldb"
)

# Cursor oluştur
mycursor = connection.cursor()

print("Connection kuruldu.....123")

# 5 sütun olduğundan 5 adet %s olmalı
sql = "INSERT INTO student(StudentNumber, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"

print(f"sql: {sql}")
# Eklenecek öğrenciler (tuple listesi)
ogrenciler = [
    ("301", "Ahmet", "Yilmaz", datetime(2006, 5, 17), "E"),
    ("302", "Ali", "Can", datetime(2005, 10, 14), "E"),
    ("303", "Canan", "Tan", datetime(2004, 11, 2), "K"),
    ("304", "Bahar", "Tokgöz", datetime(2005, 9, 22), "K")
]

print(type(ogrenciler))        # <class 'list'>
print(type(ogrenciler[0]))     # <class 'tuple'>
ogrenciler = list(ogrenciler)

try:
    mycursor.executemany(sql, ogrenciler)

    # Değişiklikleri kaydet
    connection.commit()

    print(f'{len(ogrenciler)} tane kayıt eklendi.')

except mysql.connector.Error as err:
    print("Hata:", err)

finally:
    # Bağlantıyı kapat
    connection.close()
