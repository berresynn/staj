

import mysql.connector

def urunEkle(urun_adi, fiyat):
    try:
        # MySQL bağlantısını aç
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Berre1005",
            database="node-app"
        )

        cursor = connection.cursor()

        # SQL sorgusu - tablo ismini doğru yazdık
        sql = "INSERT INTO Product (name, price) VALUES (%s, %s)"
        values = (urun_adi, fiyat)

        cursor.execute(sql, values)
        connection.commit()  # Değişiklikleri kaydet

        print(f"{cursor.rowcount} adet kayıt eklendi.")

    except mysql.connector.Error as err:
        print("MySQL Hatası:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL bağlantısı kapatıldı.")

# Örnek kullanım
urunEkle("Telefon", 7500)








